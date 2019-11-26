def select_mode():
    print('''
    Режимы:
    1 - тренировка
    0 - выход
    ''')

    mode = input('выбери режим:\n')
    while mode not in {'1', '0'}:
        print("должно быть 0 или 1")
        mode = input()

    return mode


def time_endings(digit):
    digit = str(digit)
    last_digit = digit[-1]

    if last_digit == '1':
        return 'у'
    elif 1 < int(last_digit) < 5:
        return 'ы'
    else:
        return ''


def convert_seconds(time_in_seconds):
    if time_in_seconds < 60:
        time_spent = f'{time_in_seconds} секунд'
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - 60 * minutes
        if seconds == 0:
            time_spent = f'{minutes} минут'
        else:
            time_spent = f'{minutes} минут и {seconds} секунд'

    return time_spent







