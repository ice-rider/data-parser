import json
from typing import Any


class TypeError(Exception):
    pass


class ValidationError(Exception):
    error_stack: dict[str, str] = {}
    error: dict[str, Any]
    message: str
    
    def __init__(self, error_stack: list[tuple[str, str]] | None = None):
        self.error = { 
            "error": "Validation scheme error"
        }
        
        if error_stack:
            self.error["fields"] = error_stack
        
        self.message = json.dumps(self.error, indent=2)

    def __str__(self):
        return self.message
