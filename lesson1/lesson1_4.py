largest = -1
n = int(input('Введите число '))
while n != 0:
    last_digit = n % 10
    if last_digit > largest:
        largest = last_digit
    n //= 10
print('Самая большая цифра в числе', largest)
