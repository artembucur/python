# Программа для автоматизации навыков счёта
from random import randint, choice
from timeit import default_timer

print('Привет, меня зовут Роджер. А как тебя?')
name = input() # имя
name = name.title()
print('Приятно познакомиться, ' + name)
print('Давай проверим твои знания в математике')

print('Ты готов? \'да\' или \'нет\'')
ready = input()

while ready not in {'да', 'нет'}:
    print('Ты ошибся, должно быть \'да\' или \'нет\'')
    print('Введи заново')
    ready = input()

if ready == 'да':

    # проинициализируем перменные
    examples_quantity = '' # количество примеров
    max_answer = '' # до скольки будем считать
    correct_answers = 0  # правильные ответы
    fails = 0 # ошибки
    answers_time = 0  # затраченое время

    # зададим основные условия выполнения программы и проверим их
    while not examples_quantity.isdigit():
        print(name + ', сколько примеров ты готов решить?')
        examples_quantity = input()
        if examples_quantity.isdigit():
            while int(examples_quantity) < 1:
                print('Введи число больше 0 ')
                examples_quantity = input()
                while not examples_quantity.isdigit():
                    print('Ты ошибся, должна быть цифра.')
                    examples_quantity = input()
        else:
            print('Ты ошибся, должна быть цифра.')

    while not max_answer.isdigit():
        print('До скольки будем считать? Например, до 100')
        max_answer = input()
        if max_answer.isdigit():
            while int(max_answer) < 2:
                print('Введи число больше 1')
                max_answer = input()
                while not max_answer.isdigit():
                    print('Ты ошибся, должна быть цифра.')
                    max_answer = input()
        else:
            print('Ты ошибся, должна быть цифра.')

    print('Хорошо, тогда начинаем...')

    for example in range(int(examples_quantity)):

        # случайным образом сгенерируем
        number1 = randint(1, int(max_answer))  # левый операнд
        number2 = randint(1, int(max_answer))  # правый операнд
        sign = choice('+-')  # арифметический оператор

        print('пример ' + str(example+1))

        if sign == '-':
            # исключим отрицательный ответ
            while number1 < number2:
                number1 = randint(1, int(max_answer))
            correct_answer = number1 - number2

        # вычислим результат в зависимости от операции
        if sign == '+':
            # исключим превышения максимального допустимого ответа
            while number1 + number2 > int(max_answer):
                number1 = randint(1, int(max_answer))
                number2 = randint(1, int(max_answer))
            correct_answer = number1 + number2

        # выведем текст примера и проверим введена ли цыфра
        answer = ''  # ответ

        while not answer.isdigit():
            print('сколько будет ' + str(number1) + sign + str(number2) + '?')
            start = default_timer()  # начинаем отсчёт времени
            answer = input()
            stop = default_timer()  # закончим отсчёт


            if not answer.isdigit():
                print('Ты ошибся, должна быть цифра.')

            # добавим затраченное время на один ответ в секундах
            answers_time +=round(stop-start)

        answer = int(answer)

        # проверим и подсчитаем количество правильных/неправильных ответов
        if answer == correct_answer:
            correct_answers += 1
            print('Правильно, молодец!')
        else:
            fails += 1
            print('Неправильно')
            print('правильный ответ: ' + str(correct_answer))

    if answers_time < 60:
        time_spent = f'{answers_time} секунд'
    else:
        minutes = answers_time // 60
        seconds = answers_time - 60 * minutes
        if seconds == 0:
            time_spent = f'{minutes} минут'
        else:
            time_spent = f'{minutes} минут и {seconds} секунд'

    if fails == 0:
        print(f'Молодец!, {name} Ты правильно ответил на все вопросы за {time_spent}')
    else:
        print('Правильных ответов: {}'.format(correct_answers))
        print('Ошибок: {}'.format(fails))
        print(f'Ты ответил на все вопросы за {time_spent}')


elif ready == 'нет':
    print('Передумал? Хорошо, может как-нибудь в следующий раз...')
    print('Пока!')
