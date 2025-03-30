# Task №4

# """
# Напишите функцию, которая вернет true, если массив является полностью возрастающим,
# т.е. каждый следующий элемент больше предыдущего
# """


def is_list_growing(lst: list[float]) -> bool:
    return False if lst != sorted(lst) else True


print(is_list_growing([1, 2.31, 4.4, 5]))
