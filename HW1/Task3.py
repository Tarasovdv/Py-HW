# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта
#  точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

count = 0
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

while count == 0:
    if x != 0 or y != 0:
        if x > 0 and y > 0:
            print('({x} ; {y}) -->> I четверть'.format(x=x, y=y))
        elif x < 0 and y > 0:
            print('({x} ; {y}) -->> II четверть'.format(x=x, y=y))
        elif x < 0 and y < 0:
            print('({x} ; {y}) -->> III четверть'.format(x=x, y=y))
        elif x > 0 and y < 0:
            print('({x} ; {y}) -->> IV четверть'.format(x=x, y=y))
        elif y == 0 and x != 0:
            print('({x} ; {y} -->> На оси X '.format(x=x, y=y))
        elif y != 0 and x == 0:
            print('({x} ; {y} -->> На оси Y '.format(x=x, y=y))
        count = 1
    else:
        print(
            '({x} ; {y}) -->> Точка в центре координатной плоскости '.format(x=x, y=y))
        x = int(input('Введите координату X: '))
        y = int(input('Введите координату Y: '))
