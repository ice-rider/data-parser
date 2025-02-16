# data-parser
useful data parser with graceful syntax

## Схема

Опрделение схемы парсинга производится любым из следующих способов:

### Наследование от класса Scheme
```py
from parser import Scheme, String

class LoginScheme(Scheme):
    username: String[4, 20]  # type: ignore
    password: String[8, 20]  # type: ignore
```

### создание схемы через функцию
```py
from parser import make_scheme, String, Int

register_scheme = make_scheme({
    "email":    String[5, 120],  # type: ignore
    "age":      Int[18, 100],    # type: ignore
    "username": String[4, 20],   # type: ignore
    "password": String[8, 20],   # type: ignore
})
```

для определения типов используются готовые классы поставляемые парсером:
```py
from parser import Int, String, FLoat, Bool
```

На текущий момент доступны 4 стандартных типа. Со временем их кол-во расширится.


## Использование:

для валидации данных нужно от объекта созданного класса вызвать метод `.validate(data)` и передать туда словарь
функция `register_scheme` возвращает готовый объект класса `Scheme` от которого нужно также вызвать метод `.validate(data)`

## Обработка ошибок и пример кода:

при возникновении ошибок метод `validate` создает исключение `ValidationError`

```py
from parser import ValidationError

# ... схемы определенные выше

# создадим 2 набора данных - валидный и не валидный
valid_data = {
    "username": "john_doe",
    "password": "secure123"
}

invalid_data = {
    "email": "john_doe@mail.ru",
    "age": 7,
    "username": "pro tasher mega 228 007 super cool bro"
}

try:
    LoginScheme().validate(valid_data)
    print("✅ Валидация успешна")
except ValidationError as e:
    print("❌ Ошибка валидации:")
    print(e)

try:
    register_scheme.validate(invalid_data)
    print("✅ Валидация успешна")
except ValidationError as e:
    print("❌ Ошибка валидации:")
    print(e)
```
вывод:
```py
✅ Валидация успешна
❌ Ошибка валидации:
{
  "error": "Validation scheme error",
  "fields": {
    "username": "Value pro tasher mega 228 007 super cool bro is greater than the maximum length 20.",
    "password": "Missed field"
  }
}
```
Исключение автоматически формирует объект всех ошибок в формате json.
`__str__` переопределен и возвращает строкове представление формата `json`.
Если вам нужен словарь с ошибками (т.к. зачастую в фреймворках нужен словарь) то необходимо использовать поле `ValidationErrorObject.error` представляющее собой готовое сообщение об ошибке. 
Лист `.error["fields"]` находится в `.error_stack`.
