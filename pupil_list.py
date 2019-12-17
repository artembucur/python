print('''
1. Добавить ученика
2. Список учеников
''')
mode = input('Выбери режим\n')

if mode == '1':
    name = input('Введи имя\n')
    surname = input('Введи фомилию\n')
    age = input('Введи возраст\n')

    with open('Список учеников.txt', 'a') as f:
        f.write(f'{name} {surname} {age} лет\n')
