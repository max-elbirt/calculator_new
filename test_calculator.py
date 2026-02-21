import pytest
from calculator import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_calculate():
    assert calculate("3 + 5") == 8
    assert calculate("10 - 4") == 6
    assert calculate("3 * 7") == 21
    assert calculate("15 / 3") == 5


def test_calculate_invalid_expression():
    with pytest.raises(ValueError):
        calculate("1 + 2 + 3")


def test_calculate_unknown_operator():
    with pytest.raises(ValueError, match="Unknown operator"):
        calculate("5 % 2")


def test_calculate_non_numeric():
    with pytest.raises(ValueError, match="Operands must be numbers"):
        calculate("a + b")
