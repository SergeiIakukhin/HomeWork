# Task №5

# """
# Дан список, содержащий нули. Сдвинуть все нули вправо, сохранив порядок исходного списка:
# move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]
# """


def move_zeros(lst: list[float]) -> list:
    count_zero = lst.count(0)
    for i in range(count_zero):
        lst.remove(0)
        lst.append(0)
    return lst


print(move_zeros([1, 0, 0, 3, 3, 4, 7, 10, 0, 11, 0, 0, 1]))
