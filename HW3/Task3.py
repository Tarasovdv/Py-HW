# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_list = [1.1, 1.2, 3.1, 5, 10.01]
min_float = 1
max_float = 0

for i in float_list:
    if i % 1 <= min_float and i % 1 != 0:
        min_float = round((i % 1), 2)
    if i % 1 >= max_float and i % 1 != 0:
        max_float = round((i % 1), 2)
        
print('{} - {} = {}'.format(max_float, min_float, (max_float-min_float)))
