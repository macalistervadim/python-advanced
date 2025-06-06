"""
данный пример реализует match-case
"""

# user_input = input("Введите ваше имя: ")
#
# match user_input:
#     case "Vadim":
#         print("Классное имя - Вадим!")
#     case "Aleks":
#         print("Классное имя - Алекс!")
#     case "Oleg":
#         print("Классное имя - Олег!")
#     case _:
#         raise ValueError("Такого имени нет в базе(")
#


def unpacking_db(records: dict) -> list:
    match records:
        case {"book": 2, "api": 1, "authors": [*authors]}:
            return [*authors]
        case {"book": 1, "api": 2, "authors": author}:
            return [author]
        case {"book": 0, "api": 0, "authors": 0}:
            raise ValueError("No search records in db")
        case _:
            raise ValueError("Dont match search records")


print(unpacking_db({"book": 1, "api": 2, "authors": 2}))
