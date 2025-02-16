from typing import Optional, Never

from .MetaType import MetaType, Type


class MetaString(MetaType):
    @classmethod
    def __getitem__(cls, items: tuple[int, int] | int | None) -> type[str] | None:
        """
            Method return class after initialising params (min_length, max_length)
            using:
             - String
             - String[max_length]
             - String[min_length, max_length]
        """
        _items: tuple[int, int] | tuple[int] | tuple[Never, ...] = tuple()
        
        if not isinstance(items, tuple):
            if items is None:
                _items = tuple()
            if isinstance(items, int):
                _items = (items, )

        elif not isinstance(items[0], int) or not isinstance(items[1], int):
            raise AttributeError("args must be int")
        else:
            _items = (items[0], items[1])

        attrs: dict[str, int | None] = {
            'min_length': None,
            'max_length': None
        }
        match len(_items):
            case 0:
                attrs['min_length'] = None
                attrs['max_length'] = None
            case 1:
                attrs['min_length'] = None
                attrs['max_length'] = _items[0]
            case 2:
                if len(_items) < 2:  # mypy doesn't understand 
                                    # that len(_items) is always 2 when case 2 is reached
                    return None
                attrs['min_length'] = _items[0]
                attrs['max_length'] = _items[1]
            case _:
                raise AttributeError("args length not 0, 1 or 2")

        return type(f'{cls._name}{items}', cls._bases + (Type, str), {**cls._namespace, **attrs})
