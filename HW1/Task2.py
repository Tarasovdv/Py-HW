# 2. Напишите программу для.
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('task2')
print('Дано утверждение:   ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n')

for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not (x or y or z) == (not x and not y and not z)
            print(
                f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} --->>> Утверждение: {result}')
