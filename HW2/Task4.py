# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.




n = int(input('Введите число N: '))

my_list = []
pos_list = []
mult = 1
for e in range(-n, n + 1):
    my_list.append(e)
print(my_list)


pos1 = input('Введите номер позиции 1: ')
pos_list.append(pos1)
pos2 = input('Введите номер позиции 2: ')
pos_list.append(pos2)

with open('fileTask4.txt', 'w') as data:
    for line in pos_list:
        data.write(line + '\n')

with open('fileTask4.txt', 'r') as data:
    for line in data:
        temp = int(line)
        mult *= my_list[temp-1]

print(mult)


