"""
данный пример реализует match-case
"""

user_input = input("Введите ваше имя: ")

match user_input:
    case "Vadim":
        print("Классное имя - Вадим!")
    case "Aleks":
        print("Классное имя - Алекс!")
    case "Oleg":
        print("Классное имя - Олег!")
    case _:
        raise ValueError("Такого имени нет в базе(")