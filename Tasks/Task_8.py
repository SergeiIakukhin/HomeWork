# Task №8

# """
# Выведите true, если массив содержится в другом массиве
# в том же порядке. Не обязательно элементы должны идти один
# за другим.
# contains_in_list([3, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == true
# """


def contains_in_list(small: list[int], big: list[int]) -> bool:
    if not set(small).issubset(set(big)):
        return False
    compared_sequence = []
    for el in big:
        if el in small and len(compared_sequence) < len(small):
            compared_sequence.append(el)
        elif len(compared_sequence) == len(small):
            break
        
    return compared_sequence == small


print(contains_in_list([3, 4, 8], [1, 2, 3, 5, 4, 7, 4, 8, 10]))
