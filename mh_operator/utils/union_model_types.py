from typing import Any, Dict, Optional, Type, TypeVar, Union, cast

import enum

from pydantic import BaseModel, Field, ValidationError, create_model, model_validator

E = TypeVar("E", bound=enum.Enum)
M = TypeVar("M", bound=BaseModel)


def basemodel_with_typeinfo(type_mapping: dict[E, type[M]]) -> Any:
    if not isinstance(type_mapping, dict) or not type_mapping:
        raise TypeError("type_mapping must be a non-empty dictionary.")

    (type_info_enum,) = {type(t) for t in type_mapping.keys()}
    model_union = Union[tuple(type_mapping.values())]

    def decorator(cls: type[BaseModel]) -> type[BaseModel]:
        model_name = cls.__name__

        @model_validator(mode="before")
        @classmethod
        def _validate_data_based_on_type(_, values):
            if isinstance(values, dict):
                model_type_value = values.get("model_type")
                data_payload = values.get("data")
                if model_type_value and data_payload:
                    model_type_enum = type_info_enum(model_type_value)
                    target_model = type_mapping.get(model_type_enum)
                    if target_model:
                        values["data"] = target_model.model_validate(data_payload)
            return values

        new_model = create_model(
            model_name,
            __base__=cls,
            __module__=cls.__module__,
            __validators__={"_types_validator": _validate_data_based_on_type},
            type_info=(
                type_info_enum,
                Field(description="The type info of the data field"),
            ),
            data=(
                model_union,
                Field(
                    description="The real data model, must be compatiable of the type_info field"
                ),
            ),
        )
        return cast(type[BaseModel], new_model)

    return decorator
