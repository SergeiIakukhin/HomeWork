from Tasks.Task_7 import get_pct_growth
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_7.py


@pytest.mark.parametrize(
    "lst,expected",
    [
        ([100, 150, 300, 400], ["None", "50%", "100%", "33%"]),
        ([100, 50, 300, 150], ["None", "-50%", "500%", "-50%"]),
        ([100, 125, 85, 225], ["None", "25%", "-32%", "165%"]),
    ],
)
def test_get_pct_growth(lst, expected):
    assert get_pct_growth(lst) == expected
