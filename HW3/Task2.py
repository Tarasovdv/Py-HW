# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]




my_list1 = [2, 3, 4, 5, 6]
# my_list1 = [2, 3, 5, 6]
result_list = []
half_length = (len(my_list1) + 1) // 2 #находим половину длины списка если 5 эл-тов, то = 3. 
                                       #т.е в таком случае центральный эл-т перемножаем сам на себя

for i in range(half_length):
    mult = my_list1[i] * my_list1[-1 - i]
    result_list.append(mult)

print (result_list)
