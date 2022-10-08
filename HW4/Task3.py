# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = list(map(int, input('Введите через пробел: ').split()))

task_list = []

[task_list.append(i) for i in my_list if my_list.count(i) == 1]

print('Base list: {}'.format(my_list))  
print('Task list: {}'.format(task_list))  