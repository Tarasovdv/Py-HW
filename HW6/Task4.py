# Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий, значения — словари,
# реализованные по схеме предыдущего задания.


from collections import defaultdict


def name(*names):
    name_dict = defaultdict(list)
    for item in names:
        name, second_name = item.split()
        if not name_dict.get(second_name[0]):
            name_dict[second_name[0]] = {name[0]: [item]}
        elif not name_dict[second_name[0]].get(name[0]):
            (name_dict[second_name[0]])[name[0]] = [item]
        else:
            (name_dict[second_name[0]])[name[0]].append(item)

    return dict(name_dict)


print(name("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
           "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))
