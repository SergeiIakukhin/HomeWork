from Tasks.Task_11 import calculate
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_11.py


@pytest.mark.parametrize(
    "expression,expected",
    [
        ("1-2+5", 4),
        ("1+2", 3),
        ("11-7-3+18", 19),
        ("1+21-20+9", 11),
        ("12-6+8", 14),
        ("3-5", -2),
        ("3-5-20", -22),
        ("3-5+8", 6),
    ],
)
def test_calculate(expression, expected):
    assert calculate(expression) == expected
