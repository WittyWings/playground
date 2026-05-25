import pytest
from src.calculator_service import add, subtract, multiply, divide, CalculatorError

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_invalid_input():
    with pytest.raises(CalculatorError) as exc_info:
        add("5", 3)
    assert exc_info.value.error_code == "INVALID_INPUT"
    assert "numbers" in str(exc_info.value)

def test_add_nan():
    with pytest.raises(CalculatorError) as exc_info:
        add(float('nan'), 1)
    assert exc_info.value.error_code == "INVALID_INPUT"

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_subtract_invalid_input():
    with pytest.raises(CalculatorError) as exc_info:
        subtract(5, "3")
    assert exc_info.value.error_code == "INVALID_INPUT"

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6

def test_multiply_invalid_input():
    with pytest.raises(CalculatorError) as exc_info:
        multiply(5, None)
    assert exc_info.value.error_code == "INVALID_INPUT"

def test_divide():
    assert divide(10, 2) == 5
    assert divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(CalculatorError) as exc_info:
        divide(10, 0)
    assert exc_info.value.error_code == "DIVIDE_BY_ZERO"
    assert "zero" in str(exc_info.value)

def test_divide_invalid_input():
    with pytest.raises(CalculatorError) as exc_info:
        divide("10", 2)
    assert exc_info.value.error_code == "INVALID_INPUT"

def test_divide_nan():
    with pytest.raises(CalculatorError) as exc_info:
        divide(float('nan'), 1)
    assert exc_info.value.error_code == "INVALID_INPUT"