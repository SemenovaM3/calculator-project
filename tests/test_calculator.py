# tests/test_calculator.py
from calculator import add, subtract, multiply, divide, power

def test_add():
    # Проверка сложения положительных чисел
    assert add(2, 3) == 5
    # Проверка сложения отрицательных чисел
    assert add(-1, -1) == -2
    # Проверка сложения положительного и отрицательного числа
    assert add(5, -3) == 2

def test_subtract():
    # Проверка вычитания положительных чисел
    assert subtract(5, 3) == 2
    # Проверка вычитания отрицательных чисел
    assert subtract(-1, -1) == 0
    # Проверка вычитания из меньшего числа большего
    assert subtract(3, 5) == -2

def test_multiply():
    # Проверка умножения положительных чисел
    assert multiply(2, 3) == 6
    # Проверка умножения на ноль
    assert multiply(5, 0) == 0
    # Проверка умножения отрицательных чисел
    assert multiply(-2, -3) == 6
    # Проверка умножения положительного и отрицательного числа
    assert multiply(2, -3) == -6

def test_divide():
    # Проверка деления положительных чисел
    assert divide(6, 3) == 2
    # Проверка деления отрицательных чисел
    assert divide(-6, -3) == 2
    # Проверка деления положительного числа на отрицательное
    assert divide(6, -3) == -2
    # Проверка деления с дробным результатом
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    # Проверка деления на ноль
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"

def test_power():
    # Проверка возведения в степень положительных чисел
    assert power(2, 3) == 8
    # Проверка возведения в нулевую степень
    assert power(5, 0) == 1
    # Проверка возведения нуля в степень
    assert power(0, 5) == 0
    # Проверка возведения в отрицательную степень
    assert power(2, -2) == 0.25
    # Проверка возведения отрицательного числа в степень
    assert power(-2, 3) == -8