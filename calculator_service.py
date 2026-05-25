class CalculatorError(Exception):
    """Base exception for calculator errors with an error code."""
    def __init__(self, code: str, message: str = ""):
        self.code = code
        self.message = message or code
        super().__init__(self.message)


def _validate_number(value, name: str) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    raise CalculatorError("INVALID_INPUT", f"{name} must be a number")


def add(a, b):
    a = _validate_number(a, "a")
    b = _validate_number(b, "b")
    return a + b


def subtract(a, b):
    a = _validate_number(a, "a")
    b = _validate_number(b, "b")
    return a - b


def multiply(a, b):
    a = _validate_number(a, "a")
    b = _validate_number(b, "b")
    return a * b


def divide(a, b):
    a = _validate_number(a, "a")
    b = _validate_number(b, "b")
    if b == 0:
        raise CalculatorError("DIVIDE_BY_ZERO", "Division by zero is not allowed")
    return a / b
