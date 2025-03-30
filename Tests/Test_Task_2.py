from Tasks.Task_2 import format_person
import pytest

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_2.py


@pytest.mark.parametrize(
    "fio,expected",
    [
        ("Александр cергеевич ПУШКИН", "Александр Cергеевич Пушкин"),
        ("ЯкуХин сЕРГей коНСТАнтинович", "Якухин Сергей Константинович"),
        ("якухин сергей константинович константинович", "ФИО введено некорректно"),
        ("якуХин сЕРгей", "ФИО введено некорректно"),
    ],
)
def test_format_person(fio: str, expected):
    assert format_person(fio) == expected
