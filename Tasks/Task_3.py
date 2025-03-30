# Task №3

# """
# Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
# Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
# "Иsвtrаноvв Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"
# """


def clean_name(fio: str) -> str:
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    fio = ' '.join([''.join([word[char_i].replace(word[char_i],'') if word[char_i].lower() not in alphabet else word[char_i] for char_i in range(len(word))]) for word in fio.split()])
    return fio.title()


print(clean_name('Иsвtrаноvв Ив^%ан Ива?но)вич'))
