from typing import Never

from .MetaType import MetaType, Type


class MetaInt(MetaType):
    def __getitem__(cls, items: tuple[int, int] | int | None) -> type[int] | None:
        """
            Method return class after initialising params (min, max)
            using:
             - Int
             - Int[max]
             - Int[min, max]
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
            'min': None,
            'max': None
        }
        match len(_items):
            case 0:
                pass
            case 1:
                attrs['max'] = _items[0]
            case 2:
                if len(_items) < 2:  # mypy doesn't understand
                                    # that len(_items) is always 2 when case 2 is reached
                    return None
                attrs['min'] = _items[0]
                attrs['max'] = _items[1]
            case _:
                raise AttributeError("args length not 0, 1 or 2")

        return type(f'{cls._name}{items}', cls._bases + (Type, str), {**cls._namespace, **attrs})