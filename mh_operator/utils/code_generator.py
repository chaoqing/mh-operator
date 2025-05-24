from typing import Any, Optional

import ast
import functools
import inspect
import operator
import textwrap

from .common import SingletonMeta


class _NotConstant(metaclass=SingletonMeta):
    """Sentinel class indicating a value cannot be resolved to a constant."""

    pass


_NOT_CONSTANT = _NotConstant()


# --- AST Node Value Resolution ---
def _resolve_node_to_value(node: ast.AST):
    """
    Evaluates an AST expression node to a Python value, assuming parameters are substituted.
    Returns _NOT_CONSTANT if the node cannot be resolved to a constant.
    Does not use globals, ensuring pure function evaluation.
    """
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.Name):
        # Unsubstituted names are non-constant since no globals are used.
        return _NOT_CONSTANT

    def UnaryOpEval(node: ast.UnaryOp):
        operand = _resolve_node_to_value(node.operand)
        assert operand is not _NOT_CONSTANT
        return {
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
            ast.Not: operator.not_,
            ast.Invert: operator.invert,
        }[type(node.op)](operand)

    def BinOpEval(node: ast.BinOp):
        left = _resolve_node_to_value(node.left)
        assert left is not _NOT_CONSTANT
        right = _resolve_node_to_value(node.right)
        assert right is not _NOT_CONSTANT
        return {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.LShift: operator.lshift,
            ast.RShift: operator.rshift,
            ast.BitOr: operator.or_,
            ast.BitXor: operator.xor,
            ast.BitAnd: operator.and_,
        }[type(node.op)](left, right)

    def CompareEval(node: ast.Compare):
        assert len(node.ops) == 1 and len(node.comparators) == 1
        left = _resolve_node_to_value(node.left)
        assert left is not _NOT_CONSTANT
        right = _resolve_node_to_value(node.comparators[0])
        assert right is not _NOT_CONSTANT
        return {
            ast.Eq: operator.eq,
            ast.NotEq: operator.ne,
            ast.Lt: operator.lt,
            ast.LtE: operator.le,
            ast.Gt: operator.gt,
            ast.GtE: operator.ge,
            ast.Is: operator.is_,
            ast.IsNot: operator.is_not,
        }[type(node.ops[0])](left, right)

    def BoolOpEval(node: ast.BoolOp):
        values = [_resolve_node_to_value(v) for v in node.values]
        assert all(v is not _NOT_CONSTANT for v in values)
        return all(values) if isinstance(node.op, ast.And) else any(values)

    try:
        if isinstance(node, ast.UnaryOp):
            return UnaryOpEval(node)
        elif isinstance(node, ast.BinOp):
            return BinOpEval(node)
        elif isinstance(node, ast.Compare):
            return CompareEval(node)
        elif isinstance(node, ast.BoolOp):
            return BoolOpEval(node)
        else:
            raise NotImplemented
    except:
        # Any exception means the constant evaluation failed.
        return _NOT_CONSTANT


def _value_to_ast_node(value: Any) -> ast.expr | None:
    """Converts a Python value to an AST node if it can be represented as a literal."""
    if value is None or isinstance(value, (bool, int, float, complex, str, bytes)):
        return ast.Constant(value=value)
    elif isinstance(value, list):
        elements = [v for v in map(_value_to_ast_node, value) if v is not None]
        if len(elements) == len(value):
            return ast.List(elts=elements, ctx=ast.Load())
    elif isinstance(value, tuple):
        elements = [v for v in map(_value_to_ast_node, value) if v is not None]
        if len(elements) == len(value):
            return ast.Tuple(elts=elements, ctx=ast.Load())
    elif isinstance(value, set):
        elements = [v for v in map(_value_to_ast_node, value) if v is not None]
        if len(elements) == len(value):
            return ast.Set(elts=elements)
    elif isinstance(value, dict):
        keys = [v for v in map(_value_to_ast_node, value.keys())]
        values = [v for v in map(_value_to_ast_node, value.values()) if v is not None]
        if len(values) == len(value):
            return ast.Dict(keys=keys, values=values)
    return None


class SimplifyAstTransformer(ast.NodeTransformer):
    """Simplifies ASTs through constant folding, control flow reduction, and f-string evaluation."""

    def __init__(self):
        self.changed = False

    def _try_resolve(self, node: ast.AST) -> ast.AST:
        """Attempts to resolve a node to a constant value."""
        if (value := _resolve_node_to_value(node)) is not _NOT_CONSTANT:
            if new_node := _value_to_ast_node(value):
                self.changed = True
                return ast.copy_location(new_node, node)
        return node

    def visit_UnaryOp(self, node: ast.UnaryOp) -> ast.AST:
        node.operand = self.visit(node.operand)
        return self._try_resolve(node)

    def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        return self._try_resolve(node)

    def visit_Compare(self, node: ast.Compare) -> ast.AST:
        node.left = self.visit(node.left)
        node.comparators = [self.visit(c) for c in node.comparators]
        return self._try_resolve(node)

    def visit_BoolOp(self, node: ast.BoolOp) -> ast.AST:
        node.values = [self.visit(v) for v in node.values]
        if isinstance(node.op, ast.And):
            new_values = []
            for value in node.values:
                if (resolved := _resolve_node_to_value(value)) is _NOT_CONSTANT:
                    new_values.append(value)
                elif not resolved:
                    self.changed = True
                    return ast.copy_location(ast.Constant(value=False), node)
            node.values = new_values or [ast.Constant(value=True)]
            if not new_values:
                self.changed = True
        elif isinstance(node.op, ast.Or):
            new_values = []
            for value in node.values:
                if (resolved := _resolve_node_to_value(value)) is _NOT_CONSTANT:
                    new_values.append(value)
                elif resolved:
                    self.changed = True
                    return ast.copy_location(ast.Constant(value=True), node)
            node.values = new_values or [ast.Constant(value=False)]
            if not new_values:
                self.changed = True
        if len(node.values) == 1:
            self.changed = True
            return node.values[0]
        return node

    def visit_If(self, node: ast.If) -> ast.AST | list[ast.AST]:
        node.test = self.visit(node.test)
        if (test_value := _resolve_node_to_value(node.test)) is not _NOT_CONSTANT:
            self.changed = True
            return [
                self.visit(stmt) for stmt in (node.body if test_value else node.orelse)
            ]
        node.body = [self.visit(stmt) for stmt in node.body]
        node.orelse = [self.visit(stmt) for stmt in node.orelse]
        return node

    def visit_JoinedStr(self, node: ast.JoinedStr) -> ast.AST:
        new_values = []
        current_literal = ""
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                current_literal += value.value
            elif isinstance(value, ast.FormattedValue):
                value.value = self.visit(value.value)
                if (
                    (expr_value := _resolve_node_to_value(value.value))
                    is not _NOT_CONSTANT
                    and value.conversion == -1
                    and value.format_spec is None
                ):
                    current_literal += str(expr_value)
                    self.changed = True
                else:
                    if current_literal:
                        new_values.append(ast.Constant(value=current_literal))
                        current_literal = ""
                    new_values.append(value)
            else:
                if current_literal:
                    new_values.append(ast.Constant(value=current_literal))
                    current_literal = ""
                new_values.append(value)
        if current_literal:
            new_values.append(ast.Constant(value=current_literal))
        node.values = new_values
        if len(new_values) == 1 and isinstance(new_values[0], ast.Constant):
            self.changed = True
            return new_values[0]
        return node


# --- Parameter Reassignment Checker ---
class ParamReassignChecker(ast.NodeVisitor):
    """Checks if function parameters are reassigned within the body."""

    def __init__(self, param_names: set):
        self.param_names = param_names
        self.reassigned = set()
        self.is_entry = True

    def _check_target(self, target: ast.AST):
        if isinstance(target, ast.Name) and target.id in self.param_names:
            self.reassigned.add(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self._check_target(elt)

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            self._check_target(target)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        self._check_target(node.target)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        self._check_target(node.target)
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        self._check_target(node.target)
        self.generic_visit(node)

    # Skip nested scopes
    def visit_FunctionDef(self, node: ast.FunctionDef):
        # The first function definition is the root which we should not skip
        if self.is_entry:
            self.is_entry = False
            self.generic_visit(node)

    visit_AsyncFunctionDef = visit_Lambda = visit_ClassDef = visit_FunctionDef


# --- AST Transformers ---
class InitialSubstituteTransformer(ast.NodeTransformer):
    """Replaces parameter names with their constant AST representations."""

    def __init__(self, param_values: dict[str, Any]):
        self.param_values = param_values
        self.changed = False

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if isinstance(node.ctx, ast.Load) and node.id in self.param_values:
            value = self.param_values[node.id]
            if ast_node := _value_to_ast_node(value):
                self.changed = True
                return ast.copy_location(ast_node, node)
        return node


def simplify_ast(body: list[ast.AST], max_passes: int = 10) -> list[ast.AST]:
    """Applies simplification passes to an AST body until stable or max passes reached."""
    for _ in range(max_passes):
        simplifier = SimplifyAstTransformer()
        new_body = []
        for stmt in body:
            result = simplifier.visit(stmt)
            if isinstance(result, list):
                new_body.extend(result)
            elif result is not None:
                new_body.append(result)
        body = [stmt for stmt in new_body if not isinstance(stmt, ast.Pass)] or [
            ast.Pass()
        ]
        if not simplifier.changed:
            break
    return body


# --- Helper Functions for Decorator ---
def substitute_parameters(
    func_def: ast.FunctionDef, param_values: dict[str, Any]
) -> ast.FunctionDef:
    """Substitutes function parameters with their argument values."""
    transformer = InitialSubstituteTransformer(param_values)
    transformed = transformer.visit(func_def)
    ast.fix_missing_locations(transformed)
    return transformed


def transform_return(body: list[ast.AST], return_type="none") -> list[ast.AST]:
    """Converts the last return statement to a print(json.dumps(...)) statement."""
    returns = [i for i, stmt in enumerate(body) if isinstance(stmt, ast.Return)]
    assert len(returns) < 2, f"Multiple return statements found: {len(returns)}"
    if not returns:
        return body
    return_stmt = body.pop()
    assert isinstance(
        return_stmt, ast.Return
    ), "Return statement is not the last statement"
    expr = return_stmt.value or ast.Constant(value=None)

    if return_type == "json":
        print_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[
                    ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id="json", ctx=ast.Load()),
                            attr="dumps",
                            ctx=ast.Load(),
                        ),
                        args=[expr],
                        keywords=[],
                    )
                ],
                keywords=[],
            )
        )
        ast.copy_location(print_stmt, return_stmt)
        body = [
            ast.Import(names=[ast.alias(name="json", asname=None)]),
            *body,
            print_stmt,
        ]

    if return_type == "repr":
        print_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[
                    ast.Call(
                        func=ast.Name(
                            id="repr",
                            ctx=ast.Load(),
                        ),
                        args=[expr],
                        keywords=[],
                    )
                ],
                keywords=[],
            )
        )
        ast.copy_location(print_stmt, return_stmt)
        body.append(print_stmt)

    if return_type == "asis":
        print_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[expr],
                keywords=[],
            )
        )
        ast.copy_location(print_stmt, return_stmt)
        body.append(print_stmt)

    return body


# --- Main Decorator ---
def function_to_string(return_type="repr", oneline=False):
    def decorator(func):
        """Decorator that simplifies a pure function's AST and returns its code as a string."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # get source code and parse to ast
            original_func = inspect.unwrap(func)
            source = textwrap.dedent(inspect.getsource(original_func))

            module = ast.parse(source + "\n")

            assert module.body and isinstance(
                (func_def := module.body[0]), ast.FunctionDef
            ), "Only support applying to python function"

            # make sure all parameters in function definition not reassigned
            sig = inspect.signature(original_func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            param_values = bound_args.arguments

            checker = ParamReassignChecker(set(param_values.keys()))
            checker.visit(func_def)
            assert (
                not checker.reassigned
            ), f"Parameter reassignment detected: {', '.join(checker.reassigned)}"

            # replace function parameters and simplify the body
            func_def = substitute_parameters(func_def, param_values)
            body = simplify_ast(func_def.body)
            final_body = transform_return(body, return_type=return_type)

            code = ("; " if oneline else "\n").join(
                ast.unparse(ast.fix_missing_locations(stmt))
                for stmt in final_body
                if stmt
            )
            assert not oneline or "\n" not in code, "can not oneline the function body"
            return code

        return wrapper

    return decorator
