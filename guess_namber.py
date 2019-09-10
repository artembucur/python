# Игра "Угадай чило"
import random # импортируем модуль random

print('Привет! Как тебя зовут?')
name = input() #пользовательский ввод
print('Что ж, '+ name + ', я загадал число от 1 до 20')

number = random.randint(1,20) # генерируем случайное число

counter = 1 #счетчик

for counter in range(6):
    if counter == 0:
        print('Попробуй угадать:')
    else:
        print('Попробуй ещё раз:')

    guess = int(input()) #число от пользователя которое приведём к типу integer

    if guess > number:
        print('Твоё число слишком большое')


    if guess < number:
        print('Твоё число слишком маленькое')

    if guess == number:
        break

if guess == number:
    counter = str(counter+1)
    print('Отлично, ' + name + '! Ты справился за ' + counter + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number)