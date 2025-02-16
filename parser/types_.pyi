from typing import Any, Type, TypeVar, Union, overload, Protocol, runtime_checkable, Tuple, TypeAlias, Literal

T_co = TypeVar('T_co', covariant=True)


class _BaseInt:
    min: int | None
    max: int | None
    value: int

    def __init__(self, value: int | '_BaseInt') -> None: ...


class Int(_BaseInt):
    @classmethod
    def __class_getitem__(cls, item: Union[int, Tuple[int, int]]) -> Type['IntRange']: ...


class IntRange(_BaseInt):
    min: Literal[int]  # type: ignore
    max: Literal[int]  # type: ignore


class _BaseString:
    min_length: int | None
    max_length: int | None
    value: str

    def __init__(self, value: str) -> None: ...


class String(_BaseString):
    @classmethod
    def __class_getitem__(cls, item: Union[int, Tuple[int, int]]) -> Type['StringLength']: ...


class StringLength(_BaseString):
    min_length: Literal[int]  # type: ignore
    max_length: Literal[int]  # type: ignore


class _BaseFloat:
    min: float | None
    max: float | None
    value: float

    def __init__(self, value: float) -> None: ...


class Float(_BaseFloat):
    @classmethod
    def __class_getitem__(cls, item: Union[float, Tuple[float, float]]) -> Type['FloatRange']: ...


class FloatRange(_BaseFloat):
    min: Literal[float]  # type: ignore
    max: Literal[float]  # type: ignore


class _BaseBool:
    must_have_value: bool | None
    error_msg: str | None
    value: bool

    def __init__(self, value: bool) -> None: ...


class Bool(_BaseBool):
    @classmethod
    def __class_getitem__(cls, item: Union[bool, Tuple[bool, str]]) -> Type['BoolValue']: ...


class BoolValue(_BaseBool):
    must_have_value: Literal[bool]  # type: ignore
    error_msg: Literal[str]  # type: ignore 