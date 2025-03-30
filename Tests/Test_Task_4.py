from Tasks.Task_4 import is_list_growing
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_4.py


@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 2.31, 4.4, 5], True),
        ([1, 4, 7, 22, 45], True),
        ([1, 3, 6, 3, 5], False),
        ([11, 3, 6, 9, 12], False),
    ],
)
def test_is_list_growing(lst, expected):
    assert is_list_growing(lst) == expected
