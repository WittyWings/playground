class CalculatorError(Exception):
    """Custom exception for calculator business errors."""
    def __init__(self, error_code: str, message: str):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)


def add(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise CalculatorError("INVALID_INPUT", "Both operands must be numbers")
    if any(x != x for x in [a, b]):  # Check for NaN
        raise CalculatorError("INVALID_INPUT", "Operands cannot be NaN")
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise CalculatorError("INVALID_INPUT", "Both operands must be numbers")
    if any(x != x for x in [a, b]):
        raise CalculatorError("INVALID_INPUT", "Operands cannot be NaN")
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise CalculatorError("INVALID_INPUT", "Both operands must be numbers")
    if any(x != x for x in [a, b]):
        raise CalculatorError("INVALID_INPUT", "Operands cannot be NaN")
    return a * b

def divide(a, b):
    """Divide a by b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise CalculatorError("INVALID_INPUT", "Both operands must be numbers")
    if any(x != x for x in [a, b]):
        raise CalculatorError("INVALID_INPUT", "Operands cannot be NaN")
    if b == 0:
        raise CalculatorError("DIVIDE_BY_ZERO", "Division by zero is not allowed")
    return a / b