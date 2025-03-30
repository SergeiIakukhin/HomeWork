from Tasks.Task_8 import contains_in_list
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_8.py


@pytest.mark.parametrize(
    "small, big, expected",
    [
        ([3, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
        ([3, 4, 8], [1, 2, 3, 5, 8, 7, 4, 9, 10], False),
        ([3, 4, 8], [1, 2, 3, 5, 4, 7, 4, 8, 10], False),
        ([6, 7], [1, 2, 3, 8, 9], False),
        ([6, 7], [1, 2, 6, 3, 8, 9, 7], True),
    ],
)
def test_contains_in_list(small, big, expected):
    assert contains_in_list(small, big) == expected
