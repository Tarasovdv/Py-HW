# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите число: '))
my_dict = []
sum = 0

for _ in range(1, n + 1):
    my_sequence = round((1 + 1 / _)**_, 2)
    sum += my_sequence
    my_dict.append([_, my_sequence])
    
print(dict(my_dict))
print(sum)
