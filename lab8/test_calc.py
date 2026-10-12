# Задание 4. TDD для калькулятора — тесты написаны до кода
import pytest

from calc import add, div, mul, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_mul():
    assert mul(3, 4) == 12


def test_div():
    assert div(10, 4) == 2.5


def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)
