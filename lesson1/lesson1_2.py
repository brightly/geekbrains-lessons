second = int(input('Введите время в секундах '))
hours = second // 3600
minuts = (second % 3600) // 60
seconds =  second % 60
print(f'{hours:<2}:{minuts:<2}:{seconds:<2}')