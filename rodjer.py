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

    while examples_quantity.isdigit() != True:
        print(name + ', сколько примеров ты готов решить?')
        examples_quantity = input()
        if examples_quantity.isdigit() != True:
            print('Ты ошибся, должна быть цифра.')

    while max_answer.isdigit() != True:
        print('До скольки будем считать? Например, до 100')
        max_answer = input()
        if max_answer.isdigit() != True:
            print('Ты ошибся, должна быть цифра.')

    print('Хорошо, тогда начинаем...')

    for example in range(int(examples_quantity)):
        print('пример ' + str(example+1))

elif ready == 'нет':
    print('Передумал? Хорошо, может как-нибудь в следующий раз...')
    print('Пока!')
