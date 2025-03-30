# Task №11

# """
# Реализовать калькулятор, который на входе принимает математическое
# выражение, записанное в виде строки, а возвращает вычисленное значение.
# Правила записи строки следующие:
# - скобок нет
# - только положительные числа
# - возможные операции: сложение и вычитание
# Например:
# calculate("1+2") == 3
# calculate("1+2+8") == 11
# calculate("12-6+8") == 14
# calculate("1+21-20+9") == 11
# """


def get_number(numbers: list, math_operators: list, number: str) -> (list, list):  # type: ignore
    if math_operators[-1] == "+":
        numbers.append(numbers.pop() + int(number))
        math_operators.pop()
    elif math_operators[-1] == "-":
        numbers.append(numbers.pop() - int(number))
        math_operators.pop()
    return numbers, math_operators, number


def add_char_to_list(math_operators: list, char: str):
    math_operators.append(char)
    number = ""
    return math_operators, number


def calculate(expression: str) -> int:
    numbers, math_operators, number = [], [], ""

    for char in expression:
        if char.isdigit() and char == expression[-1]:
            number += char
            numbers, *_ = get_number(numbers, math_operators, number)
        elif char.isdigit():
            number += char
        elif char in "+-":
            if numbers and math_operators:
                numbers, math_operators, number = get_number(
                    numbers, math_operators, number
                )
                math_operators, number = add_char_to_list(math_operators, char)
            else:
                numbers.append(int(number))
                math_operators, number = add_char_to_list(math_operators, char)
    return numbers[0]


print(calculate("5+16-7"))
