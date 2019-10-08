from random import randint, choice

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

    examples_quantity = '' # количество примеров
    max_answer = '' # до скольки будем считать
    correct_answers = 0  # правильные ответы
    fails = 0 # ошибки

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

    print('Хорошо, тогда начинаем...')

    for example in range(int(examples_quantity)):

        number1 = randint(1, int(max_answer))
        number2 = randint(1, int(max_answer))
        sign = choice('+-')

        print('пример ' + str(example+1))

        if sign == '-':
            while number1 < number2:
                number1 = randint(1, int(max_answer))
            correct_answer = number1 - number2

        if sign == '+':
            while number1 + number2 > int(max_answer):
                number1 = randint(1, int(max_answer))
                number2 = randint(1, int(max_answer))
            correct_answer = number1 + number2


        print(str(number1)+sign+str(number2))
        answer = int(input())

        if answer == correct_answer:
            correct_answers += 1
            print('Правильно, молодец!')
        else:
            fails += 1
            print('Неправильно')
            print('правильный ответ: ' + str(correct_answer))

    if fails == 0:
        print('Молодец!, {} Ты правильно ответил на все вопросы за '.format(name))
    else:
        print('Правильных ответов: {}'.format(correct_answers))
        print('Ошибок: {}'.format(fails))


elif ready == 'нет':
    print('Передумал? Хорошо, может как-нибудь в следующий раз...')
    print('Пока!')
