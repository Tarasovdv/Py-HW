# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Привет абв абв хай абв АБВ абвАБВ'
my_list = list(filter(lambda x: 'абв' not in x, text.split()))
print (text)
print(' '.join(my_list))