# Task №10

# """
# Напишите функцию, которая возвращает true, если скобочная последовательность
# является правильной, т.е. все открывающиеся скобки соответствуют закрывающимся.
# Скобки могут быть круглыми и квадратными.
# ((( ))) - правильно.
# [][][] - правильно
# [()][] - правильно
# [(][)] - неправильно
# ""


def are_brackets_correct(s: str) -> bool:
    brackets_sequence = []
    for bracket in s:
        if bracket in "({[":
            brackets_sequence.append(bracket)
        elif bracket in ")]}":
            if len(brackets_sequence) == 0:
                return False
            else:
                if bracket == ")" and brackets_sequence[-1] == "(":
                    brackets_sequence.pop()
                elif bracket == "]" and brackets_sequence[-1] == "[":
                    brackets_sequence.pop()
                elif bracket == "}" and brackets_sequence[-1] == "{":
                    brackets_sequence.pop()
        else:
            return False
    if not brackets_sequence:
        return True
    else:
        return False


print(are_brackets_correct("]()()"))
