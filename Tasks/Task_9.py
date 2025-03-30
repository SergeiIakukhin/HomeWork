# Task №9

# """
# Напишите функцию, которая парсит строку в формате ключ-значение
# и возвращает соответствующий словарь.
# Для продвинутых: при ошибке ввода (повторяющиеся ключи, например)
# выбрасывать исключение. Подумайте о других возможных ошибках.
# Пример:
# actual = parse_dict('first_name="Alex", last_name="Pushkin"')
# expected = {
#     'first_name': 'Alex',
#     'last_name': 'Pushkin'
# }
# """


def parse_dict(d_str: str) -> dict[str, str]:
    d_str = [[word for word in element.strip().split("=")] for element in d_str.split(",")]
    dictionary = {key: value for key, value in d_str}
    return dictionary


print(parse_dict('first_name="Alex", last_name="Pushkin"'))


# def parse_dict_2(d_str: str) -> dict[str, str]:
#     d_str = [[word for word in element.strip().split("=")] for element in d_str.split(",")]
#     dictionary = {}
#     for key, value in d_str:
#         if key not in dictionary:
#             dictionary[key] = value
#         else:
#             print(f'Хотите перезаписать ключ {key} со значением {dictionary.get(key)} на значение {value}?')
#             if input('Введите YES или NO: \n') == 'YES': dictionary[key] = value             
#     return dictionary

# print(parse_dict_2('last_name="Pushkin", first_name="Alex", last_name="Iakukhin", first_name="Sergey"'))