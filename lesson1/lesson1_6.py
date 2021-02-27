a = int(input())
b = int(input())
day = 1
while a < b:
    a += a * 0.1
    day += 1
print(f'на {day} спортсмен пробежит не меньше {b} км')
