# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.

from collections import defaultdict


names = "Иван, Мария, Петр, Илья, Марина, Петр, Алина, Бибочка"


# Variant 1 для строки с именами
def name(n):
    arr = n.split(", ")
    name_dict = defaultdict(list)
    for x in arr:
        name_dict[x[0]].append(x)
    return dict(name_dict)


print(name(names))


# Variant 2 Для переменных в функции
def name2(*names):
    name_dict = defaultdict(list)
    for x in names:
        name_dict[x[0]].append(x)
    return dict(name_dict)


print(name2("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
