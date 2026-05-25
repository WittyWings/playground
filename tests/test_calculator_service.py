import pytest
from calculator_service import add, subtract, multiply, divide, CalculatorError

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-5, 5, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add_happy(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (10, -5, 15),
    (2.5, 1.5, 1.0),
])
def test_subtract_happy(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 10, 0),
    (1.5, 2, 3.0),
])
def test_multiply_happy(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (7.5, 2.5, 3.0),
])
def test_divide_happy(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(CalculatorError) as exc:
        divide(10, 0)
    assert exc.value.code == "DIVIDE_BY_ZERO"

def test_invalid_operand():
    with pytest.raises(CalculatorError) as exc:
        add("a", 2)
    assert exc.value.code == "INVALID_INPUT"
