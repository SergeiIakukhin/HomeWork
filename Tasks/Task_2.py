# Task №2

# """
# Дана ФИО, возможно с маленькой буквы, возможно с большой.
# Написать функцию, которая делает фамилию, имя и отчество с большой буквы,
# а остальные буквы должны быть маленькими.
# "Александр cергеевич ПУШКИН" -> "Александр Cергеевич Пушкин".
# Не будем использовать встроенную функцию title()
# """


def format_person(fio: str) -> str:
    if len(fio.split()) != 3: return 'ФИО введено некорректно'
    fio = ' '.join([''.join([word[i_char].upper() if i_char == 0 else word[i_char].lower() for i_char in range(len(list(word)))]) for word in fio.split()])
    return fio

print(format_person('Александр cергеевич ПуШкин'))