# tests/test_calculator.py
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"