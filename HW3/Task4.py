# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = int(input('Введите десятичное число: '))


# variant1
# divisible = n  # делимое
# divisor = 2  # делитель
# remainder_my = 1
# my_bin = ''

# while remainder_my > 0:
#     my_bin = str(divisible % divisor) + my_bin
#     remainder_my = (divisible)//divisor
#     divisible = remainder_my
# print(my_bin)


# variant2
print(bin(n)[2:])
