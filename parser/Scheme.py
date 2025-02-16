from __future__ import annotations
from typing import Any, Type, TypeVar, Generic, TypeAlias, Union
import json

from .types_ import Int, String, Float, Bool
from .Exception import ValidationError


T_co = TypeVar('T_co', covariant=True)


AnySchemeType: TypeAlias = Union[Type[Int], Type[String], Type[Float], Type[Bool]]


class SchemeType(Generic[T_co]):
    """Тип для полей схемы"""
    def __init__(self, type_class: Type[T_co]):
        self.type_class = type_class


class Scheme:
    """Базовый класс для схем"""
    scheme: dict[str, SchemeType[Any]] = {}

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.scheme = {}
        
        # Получаем все аннотации типов
        annotations = cls.__annotations__
        
        for field_name, field_type in annotations.items():
            # Проверяем является ли тип встроенным
            if field_type in (int, str, float, bool):
                # Конвертируем встроенные типы в наши кастомные
                if field_type == int:
                    cls.scheme[field_name] = SchemeType(Int)
                elif field_type == str:
                    cls.scheme[field_name] = SchemeType(String)
                elif field_type == float:
                    cls.scheme[field_name] = SchemeType(Float)
                elif field_type == bool:
                    cls.scheme[field_name] = SchemeType(Bool)
            else:
                if hasattr(field_type, '__origin__'):
                    base_type = field_type.__origin__
                    params = field_type.__args__
                    cls.scheme[field_name] = SchemeType(base_type[params])
                else:
                    cls.scheme[field_name] = SchemeType(field_type)

    def validate(self, data: dict):
        if not self.scheme:
            raise ValueError("Scheme is not defined")
        
        error_fields = {}

        for property_, type_ in self.scheme.items():
            if property_ not in data.keys():
                error_fields[property_] = "Missed field"
                continue

            try:
                type_.type_class(data[property_])
            except ValueError as e:
                error_fields[property_] = str(e)
            except Exception as e:
                error_fields[property_] = f"handling error: {str(e)}"

        if error_fields:
            raise ValidationError(error_fields)


def make_scheme(scheme: dict[str, AnySchemeType]) -> Scheme:
    """
    Создает схему из словаря типов.
    
    Пример:
        scheme = make_scheme({
            "username": String[4, 20],  # Вернет StringLength
            "age": Int[18, 100]         # Вернет IntRange
        })
    """
    scheme_obj = Scheme()
    scheme_obj.scheme = {key: SchemeType(type_class) for key, type_class in scheme.items()}
    return scheme_obj
