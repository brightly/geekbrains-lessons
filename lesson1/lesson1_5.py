costs = int(input('Введите издержки в вашей компании '))
profit = int(input('Введите прибыль вашей компании '))
if costs > profit:
    print('Мне жаль, но ваша компания убыточна')
elif costs == profit:
    print('Вы сработали в ноль')
else:
    worker = int(input('Сколько сотруднков в вашей компании '))
    print('На каждого сотрудника приходится', (profit-costs)/worker, 'рублей прибыли')