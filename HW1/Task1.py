# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('task1')
count = 0
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

index = int(input('Введите число, обозначающее день недели: '))

while count == 0:
    if int(index < 8) and int(not index < 1):
        if 0 < index < 6:
            print(week_days[index-1] + ' -> Рабочий день!')
        elif 5 < index < 8:
            print(week_days[index-1] + ' -> Выходной день!')
        count = 1

    else:
        print('Вы ввели не существующий день недели')
        index = int(input('Введите число, обозначающее день недели: '))
