import ast
import operator
from typing import Any

# Mapping of AST operators to actual functions
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

def _eval(node: ast.AST) -> Any:
    if isinstance(node, ast.Num):  # <number>
        return node.n
    if isinstance(node, ast.BinOp):  # <left> <operator> <right>
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            try:
                return _OPERATORS[op_type](left, right)
            except ZeroDivisionError:
                raise CalculatorError("division by zero")
        else:
            raise CalculatorError(f"unsupported operator: {op_type}")
    if isinstance(node, ast.UnaryOp):  # - <operand> e.g., -1
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            return _OPERATORS[op_type](operand)
        else:
            raise CalculatorError(f"unsupported unary operator: {op_type}")
    raise CalculatorError(f"unsupported expression: {type(node)}")

def evaluate_expression(expression: str) -> float:
    """Safely evaluate a simple arithmetic expression.

    Supports +, -, *, /, %, ** and unary minus.
    Raises CalculatorError for invalid inputs.
    """
    # Validate allowed characters
    if not all(c.isdigit() or c.isspace() or c in "+-*/%().**" for c in expression):
        raise CalculatorError("invalid characters in expression")
    try:
        node = ast.parse(expression, mode='eval')
        return _eval(node.body)
    except (SyntaxError, ValueError) as e:
        raise CalculatorError("malformed expression")
