from random import shuffle
from time import sleep

cards = [6,7,8,9,10,11]*4
your_points = 0
bot_points = 0
shuffle(cards)

def move(points):
    card = cards.pop()
    points += card

    print(f'''
    Очки: {points}
    Вам выпало: {card}
    ''') 
    return points

play_again = "да"
while play_again == "да":
    print("Ваш ход:")
    your_points = move(your_points)
    sleep(2)
    print("Ход бота:")
    bot_points = move(bot_points)
    if your_points > 21:
        print("Вы проиграли")
        break
    elif your_points == 21:
        print("Вы победили")
        break
    else:
        play_again = input("Вытянуть карту ещё? да\нет\n")

   