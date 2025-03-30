from Tasks.Task_5 import move_zeros
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_5.py


@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 0, 0, 2, 3, 0, 1], [1, 2, 3, 1, 0, 0, 0]),
        (
            [1, 0, 0, 3, 3, 4, 7, 10, 0, 11, 0, 0, 1],
            [1, 3, 3, 4, 7, 10, 11, 1, 0, 0, 0, 0, 0],
        ),
        ([0, 0, 0, 1, 0, 2, 0, 0, 5, 0], [1, 2, 5, 0, 0, 0, 0, 0, 0, 0]),
    ],
)
def test_move_zeros(lst, expected):
    assert move_zeros(lst) == expected
