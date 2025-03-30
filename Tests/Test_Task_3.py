from Tasks.Task_3 import clean_name
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_3.py


@pytest.mark.parametrize(
    "fio,expected",
    [
        ("Иsвtrаноvв Ив^%ан Ива?но)вич", "Иванов Иван Иванович"),
        (
            "YadЯкуh^&хин #Серggгgей kooКонстан#$@тинович",
            "Якухин Сергей Константинович",
        ),
        (
            "Yadякуh^&хин #Серggгgей kooконстан#$@тинович",
            "Якухин Сергей Константинович",
        ),
    ],
)
def test_clean_name(fio, expected):
    assert clean_name(fio) == expected
