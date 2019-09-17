#игра "угадай число"
import random, time

def displayIntro():
    print('''Вы находжтесь в зземлях, заселённых драконами.
    Пред собой вы видите две пещеры.
    В одной из них - дружелюбный дракон,который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.
    ''')

def chooseCave():
    print('В какую пещеру вы пойдёте нажмите клавишу (1 или 2)')
    choosen_cave = int(input())
    return choosen_cave

def checkCave(cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(3)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(3)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    time.sleep(3)

    friendly_cave = random.randint(1, 2)

    if cave == friendly_cave:
        print('делится своими сокровищами')
    else:
        print('моментально вас съедает')

displayIntro()
checkCave(chooseCave())