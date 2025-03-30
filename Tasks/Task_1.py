# Task №1

# """
# Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
# от числа N. Например, 1 просмотр, 2 просмотра и т.п.
# """


def get_views_count(n: int) -> str:
    variants_word = ["просмотр", "просмотров", "просмотра"]
    if n < 10:
        if n % 10 == 1:
            return f"{n} {variants_word[0]}"
        elif (n % 10 == 0) or (5 <= n % 10 <= 9):
            return f"{n} {variants_word[1]}"
        else:
            return f"{n} {variants_word[2]}"
    elif n > 9 and 0 <= n % 100 <= 9:
        if n % 100 == 1:
            return f"{n} {variants_word[0]}"
        elif (n % 100 == 0) or (5 <= n % 100 <= 9):
            return f"{n} {variants_word[1]}"
        else:
            return f"{n} {variants_word[2]}"
    elif n > 9 and 10 <= n % 100 <= 20:
        return f"{n} {variants_word[1]}"
    else:
        if ((n % 100) % 10) == 1:
            return f"{n} {variants_word[0]}"
        elif 2 <= ((n % 100) % 10) <= 4:
            return f"{n} {variants_word[2]}"
        else:
            return f"{n} {variants_word[1]}"


print(get_views_count(10175))
