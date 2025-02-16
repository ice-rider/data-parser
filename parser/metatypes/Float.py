from typing import Never

from .MetaType import MetaType, Type


class MetaFloat(MetaType):
    def __getitem__(cls, items: tuple[float, float] | float | None) -> type[float] | None:
        """
            Method return class after initialising params (min, max)
            using:
             - Float
             - Float[max]
             - Float[min, max]
        """
        _items: tuple[float, float] | tuple[float] | tuple[Never, ...] = tuple()

        if not isinstance(items, tuple):
            if items is None:
                _items = tuple()
            if isinstance(items, float):
                _items = (items, )

        elif not isinstance(items[0], float) or not isinstance(items[1], float):
            raise AttributeError("args must be float")
        else:
            _items = (items[0], items[1])

        attrs: dict[str, float | None] = {
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
                raise AttributeError("args must be tuple of 0, 1 or 2 floats")

        return type(f'{cls._name}{items}', cls._bases + (Type, str), {**cls._namespace, **attrs})
