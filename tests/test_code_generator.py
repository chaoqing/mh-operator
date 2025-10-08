from mh_operator.utils.code_generator import function_to_string


@function_to_string(return_type="repr", oneline=True)
def simple_math(a, b=2):
    c = a * b
    d = c + 10
    return d


@function_to_string(return_type="repr", oneline=False)
def if_logic(x, y):
    res = 0
    if x > y + 2:
        res = x - y
    else:
        res = x + y
    return res


@function_to_string(return_type="json", oneline=False)
def fstring_and_return_transform(name, val):
    msg = f"Hello {name}, your calculated value is {val}."
    return {"message": msg, "original_age": val}  # Complex return


@function_to_string(return_type="none")
def no_return(val):
    if val > 10:
        processed = val * 100


@function_to_string()
def only_pass():
    pass


@function_to_string(return_type="repr", oneline=False)
def becomes_pass(a):
    if a > 100 and a < 0:  # Always false
        b = 10
    return None


def test_simplify_pure_function_ast():
    print("--- simple_math(5) ---")
    print(simple_math(5))
    # Expected: c = 10; d = 20; import json; print(json.dumps(20))

    print("\n--- if_logic(10, 5) ---")
    print(if_logic(10, 5))
    # Expected: res = 5; import json; print(json.dumps(5))

    print("\n--- if_logic(5, 5) ---")
    print(if_logic(5, 5))
    # Expected: res = 10; import json; print(json.dumps(10))

    print("\n--- fstring_and_return_transform('User', 25) ---")
    print(fstring_and_return_transform("User", 25))
    # Expected: val = 30; msg = f"Hello User, your calculated value is 30."; import json; print(json.dumps({'message': msg, 'original_age': 25}))
    # The f-string itself might not fully simplify if 'name' remains symbolic.

    print("\n--- no_return(15) ---")
    print(no_return(15))
    # Expected: processed = 1500 (if print inside is removed or simplified)
    # Or if the print is symbolic: if 15 > 10: processed = 1500; print(f"Processed value: {processed}")
    # Current simplifier doesn't remove print statements. If no return, output is just the simplified body.

    print("\n--- only_pass() ---")
    print(only_pass())
    # Expected: pass

    print("\n--- becomes_pass(10) ---")
    print(becomes_pass(10))
    # Expected: import json; print(json.dumps(None)); pass (or just the print if pass gets fully optimized out)
    # More likely: import json; print(json.dumps(None)) if last pass auto-removed

    # Test parameter reassignment error
    print("\n--- reassign(5) ---")
    try:

        @function_to_string(return_type="repr", oneline=False)
        def reassign(a):
            for a in range(10):
                pass  # This should cause an assertion error

            return a

        print(reassign(5))
    except Exception as e:  # Catching the broad error from the decorator for testing
        print(f"Caught expected error: {e}")


def test_columns():
    from mh_operator.legacy.UnknownsAnalysisDataSet import ProcessedColumns

    ProcessedColumns2 = (
        ("SampleID", int, "The sample ID in this uaf file"),
        ("StartX", float, "The start retention time of this compound"),
        ("RetentionTime", float, "The retention time of this compound"),
        ("EndX", float, "The end retention time of this compound"),
        ("CompoundName", str, "The compound name"),
        ("CASNumber", str, "The compound CAS number"),
        ("Formula", str, "The compound formula"),
        (
            "LibraryMatchScore",
            float,
            "The compound library match score, range 0 to 100",
        ),
        ("MolecularWeight", float, "The compound molecular weight"),
        ("Area", float, "The compound area"),
        ("Height", float, "The compound height"),
        ("EstimatedConcentration", float, "The compound estimated concentration"),
    )

    for c, c2 in zip(ProcessedColumns, ProcessedColumns2):
        assert c.fget.__name__ == c2[0]
