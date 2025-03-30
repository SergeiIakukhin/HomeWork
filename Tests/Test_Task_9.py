from Tasks.Task_9 import parse_dict
import pytest


# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_9.py


@pytest.mark.parametrize(
    "d_str, expected",
    [
        (
            'first_name="Alex", last_name="Pushkin"',
            {"first_name": '"Alex"', "last_name": '"Pushkin"'},
        ),
        (
            'first_name="Alex", last_name="Pushkin", first_name="Sergey", last_name="Iakukhin"',
            {"first_name": '"Sergey"', "last_name": '"Iakukhin"'},
        ),
        (
            'first_name="Sergey", last_name="Iakukhin", mob_phone=+79045116789, email=parivet@mail.com',
            {
                "first_name": '"Sergey"',
                "last_name": '"Iakukhin"',
                "mob_phone": "+79045116789",
                "email": "parivet@mail.com",
            },
        ),
    ],
)
def test_parse_dict(d_str, expected):
    assert parse_dict(d_str) == expected
