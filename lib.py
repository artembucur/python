def summa(x,y):
    sum = x + y
    print(f'сумма числа {x} и {y} равна {sum}')


def time_endings(digit):
    digit = str(digit)
    last_digit = digit[-1]

    if last_digit == '1':
        return 'у'
    elif 1 < int(last_digit) < 5:
        return 'ы'
    else:
        return ''