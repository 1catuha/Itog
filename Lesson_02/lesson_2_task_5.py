def month_to_season(month):
    if month in [1, 2, 12]:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца: "))
season = month_to_season(month)


print(f"Месяц {month} относится к сезону {season}")
