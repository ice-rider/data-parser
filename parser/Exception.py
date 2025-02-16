import json


class TypeError(Exception):
    pass


class ValidationError(Exception):
    error_stack: dict[str, str] = {}
    message: str
    
    def __init__(self, error_stack: list[tuple[str, str]] | None = None):
        if error_stack is None:
            self.message = "{\n\t\"error\": \"Validation scheme error\"\n}"
        else:
            self.message = self.make_message_json(error_stack)

    @staticmethod
    def make_message_json(error_stack: list[tuple[str, str]]) -> str:
        return json.dumps({
            "error": "Validation scheme error",
            "fields": error_stack
        }, indent=2)
        
    def __str__(self):
        return self.message
