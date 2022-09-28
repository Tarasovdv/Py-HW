# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер ЧЕТВЕРТИ координатной плоскости: '))
count = 0
while count == 0:
    if 0 < quarter_number < 5:
        if quarter_number == 1:
            print(
                '(I) -->> 0 < X ; 0 < Y ')
        elif quarter_number == 2:
            print(
                '(II) -->> X < 0; 0 < Y ')
        elif quarter_number == 3:
            print(
                '(III) -->> X < 0; Y < 0 ')
        elif quarter_number == 4:
            print(
                '(IV) -->> 0 < X; Y < 0 ')
        count = 1
    else:
        print('Такой четчети не существует!')
        quarter_number = int(input('Введите номер ЧЕТВЕРТИ координатной плоскости: '))
