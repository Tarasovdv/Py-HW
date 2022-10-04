# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# item[START:STOP:STEP] СРЕЗ
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# variant 1
print(sum(my_list[1::2])) # начинаем с первого (индекс) до конца с шагом 2 = все элементы с НЕЧЕТ индексами(позиции)

# variant 2 
# odd_elem_list = []
# sum_odd_elem = 0
# print('Base list -->> ', my_list)
# for i, elem in enumerate(my_list):
#     if i % 2 != 0:
#         odd_elem_list.append(elem)
#         sum_odd_elem += elem
# print('odd_elem_list -->> ', odd_elem_list)
# print('sum_odd_elem -->> ', sum_odd_elem)
