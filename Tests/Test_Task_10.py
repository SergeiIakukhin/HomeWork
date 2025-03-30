from Tasks.Task_10 import are_brackets_correct
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_10.py


@pytest.mark.parametrize(
    "s,expected",
    [
        ("((()))", True),
        ("[][][]", True),
        ("[()][]", True),
        ("[(][)]", False),
        ("", True),
    ],
)
def test_are_brackets_correct(s, expected):
    assert are_brackets_correct(s) == expected
