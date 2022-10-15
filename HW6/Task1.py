
# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
import random

while True:
    try:
        count = int(input("Enter number of count: "))
        number = [(random.randint(1, 100)) for x in range(count)]
        num_filt = [j for i, j in zip(number, number[1:]) if j > i]
        break
    except ValueError:
        print("You entered not number. Try again! ")

print("Source list: " + (", ").join(map(str, number)))
print("Resuit: " + (", ").join(map(str, num_filt)))
