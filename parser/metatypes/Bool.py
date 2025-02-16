from typing import Never

from .MetaType import MetaType, Type


class MetaBool(MetaType):
    def __getitem__(cls, items: tuple[bool, str] | bool | None):
        """
            Method return class after initialising params (value)
            using:
             - Bool
             - Bool[value]             # value is required value for example if user must agree with something 
             - Bool[value, error_msg]  # error_msg is message that will be shown if input is bool but isn't value
        """
        _items: tuple[bool, str] | tuple[bool] | tuple[Never, ...] = tuple()

        if not isinstance(items, tuple):
            if items is None:
                _items = tuple()
            if isinstance(items, bool):
                _items = (items, )

        elif not isinstance(items[0], bool):
            raise AttributeError("args must be bool")
        else:
            _items = (items[0], items[1])

        attrs: dict[str, bool | str | None] = {
            'must_have_value': None,
            'error_msg': None
        }
        match len(_items):
            case 0:
                pass
            case 1:
                attrs['must_have_value'] = _items[0]
            case 2:
                if len(_items) < 2:  # mypy doesn't understand
                                    # that len(_items) is always 2 when case 2 is reached
                    return None
                attrs['must_have_value'] = _items[0]
                attrs['error_msg'] = _items[1]
            case _:
                raise AttributeError("args length not 0, 1 or 2")

        return type(f'{cls._name}{items}', cls._bases + (Type, str), {**cls._namespace, **attrs})
