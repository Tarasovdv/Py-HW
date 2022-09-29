# Реализуйте алгоритм перемешивания списка.без shuffle

from random import randint


n = 10
my_arr = []

for i in range(n+1):
    my_arr.append(i)
print('Base Array:    {}'.format(my_arr))

len_arr = len(my_arr)


for e in range(len_arr):
    j = randint(0, len_arr-1)
    el = (my_arr.pop(j))
    my_arr.append(el)
print('Shuffle Array: {}'.format(my_arr))