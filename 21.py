from random import shuffle, choice
from time import sleep
 
cards = ["Валет","Дама","Король","Туз"]
masti = ["черви",'бубны','крестьи','пики']

koloda = []
for mast in masti:
    for card in range(2,11):
        koloda.append(f"{card} {mast}")
    for card in cards:
        koloda.append(f"{card} {mast}")

shuffle(cards)

your_points = 0
bot_points = 0
moves = 1


def receive_card_points(card):
    received_card = card.split()
    first = {"Валет":"J","Дама":"Q","Король":"K","Туз":"T"}

    cards_points = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,first["Валет"]:10,first["Дама"]:10,first["Король"]:10,first["Туз"]:choice([1,11])}
    print(cards_points)
    return cards_points[card[0]]


def move(points):
    card = koloda.pop()
    card_point = receive_card_points(card)
    points += card_point

    print(f'''
    Очки: {points}
    Вам выпало: {card}
    ''') 
    return points


def check_points(bot_points, user_points):
    
    if bot_points > 21:
        print("Вы выиграли")
        return False
    elif bot_points == user_points:
        print("Ничья")
        return False
    else:
        return True

play_again = "да"
while play_again == "да":
    
    if moves == 1:
        for _ in range(2):
            print("Ваш ход:")
            your_points = move(your_points)
            sleep(2)
    else:
        print("Ваш ход:")
        your_points = move(your_points)
        sleep(2)
    
    if your_points > 21:
        print("Вы проиграли")
        break
    elif your_points == 21:
        print("Black Jack!!!")
        play_again = "нет"
    else:
        play_again = input("Вытянуть карту ещё? да или нет\n")    
else:
        go = True
        while go:
            if bot_points < 18:
                print("Ход бота:")
                bot_points = move(bot_points)
                go = check_points(bot_points, your_points)
            else:
                check_points(bot_points, your_points)
                go = False

            

   