# Task №6

# """
# Дан список целых чисел и определенное заданное число. Найти все пары из списка, сумма которых равна этому числу.
# Верните из функции список кортежей.
# Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
# """


def get_pairs_number(lst: list[int], n) -> list[tuple]:
    lst = list(set(lst))
    list_tuples = []
    lst = [list_tuples.append(tuple([i, j])) for j in lst for i in lst if i + j == n and tuple([j, i]) not in list_tuples and j != i]
    return list_tuples if list_tuples else []


print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))
