from typing import Any, Type, TypeVar, Generic, Dict, Protocol, TypeAlias, Union

from .types import (
    Int, String, Float, Bool,
    IntRange, StringLength, FloatRange, BoolValue
)


T_co = TypeVar('T_co', covariant=True)


# Тип для любого из наших типов
AnySchemeType: TypeAlias = Union[
    Type[Int], Type[String], Type[Float], Type[Bool],
    Type[IntRange], Type[StringLength], Type[FloatRange], Type[BoolValue]
]


class SchemeType(Generic[T_co]):
    type_class: Type[T_co]

    def __init__(self, type_class: Type[T_co]) -> None: ...


class Scheme:
    scheme: Dict[str, SchemeType[Any]]

    def validate(self, data: dict) -> None: ...


def make_scheme(scheme: Dict[str, AnySchemeType]) -> Scheme: ... 