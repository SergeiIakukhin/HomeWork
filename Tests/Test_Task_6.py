from Tasks.Task_6 import get_pairs_number
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_6.py


@pytest.mark.parametrize(
    "lst, n, expected",
    [
        ([1, 2, 4, 3, 5, 2], 5, [(4, 1), (3, 2)]),
        ([1, 2, 4, 3, 5, 2], 7, [(5, 2), (4, 3)]),
        ([5, 9, 24, 11, 5, 13], 24, [(13, 11)]),
        ([5, 9, 24, 11, 5, 13], 14, [(9, 5)]),
        ([], 7, []),
        ([5, 9, 24, 11, 5, 13], 11, []),
    ],
)
def test_get_pairs_number(lst, n, expected):
    assert get_pairs_number(lst, n) == expected
