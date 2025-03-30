from Tasks.Task_1 import get_views_count
import pytest

# variants_word = ["просмотр", "просмотров", "просмотра"]

# Чтобы запустить тест для этого файла, введите в терминале: pytest Tests\Test_Task_1.py


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1 просмотр"),
        (21, "21 просмотр"),
        (101, "101 просмотр"),
        (221, "221 просмотр"),
        (451, "451 просмотр"),
        (1001, "1001 просмотр"),
    ],
)
def test_get_views_count_first_variant_word(n, expected):
    assert get_views_count(n) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, "0 просмотров"),
        (5, "5 просмотров"),
        (10, "10 просмотров"),
        (100, "100 просмотров"),
        (211, "211 просмотров"),
        (575, "575 просмотров"),
        (1000000, "1000000 просмотров"),
    ],
)
def test_get_views_count_second_variant_word(n, expected):
    assert get_views_count(n) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, "2 просмотра"),
        (4, "4 просмотра"),
        (22, "22 просмотра"),
        (74, "74 просмотра"),
        (102, "102 просмотра"),
        (222, "222 просмотра"),
        (1003, "1003 просмотра"),
    ],
)
def test_get_views_count_third_variant_word(n, expected):
    assert get_views_count(n) == expected
