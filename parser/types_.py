from __future__ import annotations
from typing import Any, TypeVar, overload, Union, Type

from .metatypes import MetaInt, MetaString, MetaFloat, MetaBool


T = TypeVar('T')


class Int(metaclass=MetaInt):  # type: ignore
    min: int | None = None
    max: int | None = None

    def __init__(self, value: int | Int):
        if not isinstance(value, int):  # type match
            raise ValueError(f"Value {value} is not an integer.")
        if self.min is not None and value < self.min:  # value match
            raise ValueError(f"Value {value} is less than the minimum {self.min}.")
        if self.max is not None and value > self.max:  # value match
            raise ValueError(f"Value {value} is greater than the maximum {self.max}.")
        self.value = value


class String(metaclass=MetaString):  # type: ignore
    min_length: int | None = None
    max_length: int | None = None

    def __init__(self, value: str):
        if not isinstance(value, str):  # type match
            raise ValueError(f"Value {value} is not a string.")
        if self.min_length is not None and len(value) < self.min_length:  # length match
            raise ValueError(f"Value {value} is less than the minimum length {self.min_length}.")
        if self.max_length is not None and len(value) > self.max_length:  # length match
            raise ValueError(f"Value {value} is greater than the maximum length {self.max_length}.")
        self.value = value


class Float(metaclass=MetaFloat):  # type: ignore
    min: float | None = None
    max: float | None = None

    def __init__(self, value: float):
        if not isinstance(value, float):  # type match
            raise ValueError(f"Value {value} is not a float.")
        if self.min is not None and value < self.min:  # value match
            raise ValueError(f"Value {value} is less than the minimum {self.min}.")
        if self.max is not None and value > self.max:  # value match
            raise ValueError(f"Value {value} is greater than the maximum {self.max}.")
        self.value = value


class Bool(metaclass=MetaBool):  # type: ignore
    must_have_value: bool | None = None
    error_msg: str | None = None

    def __init__(self, value: bool):
        if not isinstance(value, bool):  # type match
            raise ValueError(f"Value {value} is not a boolean.")
        if self.must_have_value is not None and value != self.must_have_value:  # value match
            if self.error_msg is not None:
                raise ValueError(self.error_msg)
            raise ValueError(f"Value {value} is not the required value {self.must_have_value}.")
        self.value = value
