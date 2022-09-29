# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

mult_dict = []
num_dict = []
mult = 1
n = int(input('Enter number: '))
for _ in range(1, n + 1):
    mult *= _
    mult_dict.append(mult)
    num_dict.append(_)

print('{} -->> {}'.format(num_dict, mult_dict))
