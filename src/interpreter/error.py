from enum import Enum
class ErrorType(Enum):
    ERROR = 0
    WARN = 1

class Error:
    errType = ErrorType(0)
    name = "UndefinedError"

    def __init__(self, type: ErrorType, name: str):
        """
        Create a new Error.

        :param type: The type of error [ErrorType enum, or 0 for error, 1 for warning.]
        :param name: The name of the error [i.e. TimedOutError].
        """
    self.errType = type
    self.name = name
    
    