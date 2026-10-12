# Калькулятор, написанный по TDD (сначала тесты в test_calc.py)
import logging

logger = logging.getLogger(__name__)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        logger.error("Деление на ноль")
        raise ValueError("Деление на ноль")
    return a / b
