from abc import ABC, abstractmethod
from typing import List, Any


class MetaType(type, ABC):
    _name:       str = None
    _bases:      tuple[type] = None
    _namespace:  dict = None
    
    def __init__(self, name, bases, namespace):
        cls = self.__class__
        cls._name = name
        cls._bases = bases
        cls._namespace = namespace

    def __new__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]):
        return super().__new__(cls, name, bases, attrs)

    @abstractmethod
    def __getitem__(self, args: tuple):
        pass


class Type(metaclass=MetaType):
    value: Any
    
    def __init__(self, value: Any) -> None:
        pass
