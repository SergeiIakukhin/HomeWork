# Task №7

# """
# Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
# Для первого элемента списка выведите значение None. Округлите до целых.
# Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
# """


def get_pct_growth(lst: list[float]) -> list[str]:
    rate_of_increase = [str(None) if i == 0 else str(round(((lst[i] - lst[i-1]) / lst[i-1])*100)) + '%' for i in range(len(lst))]
    return rate_of_increase


print(get_pct_growth([100, 125.5, 85, 225.5]))
