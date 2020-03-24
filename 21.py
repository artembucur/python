from random import shuffle, choice
from time import sleep
 

def get_deck():
    deck = []
    for suit in ("черви",'бубны','крестьи','пики'):
        for card in range(2,11):
            deck.append(f"{card} {suit}")
        for card in ("валет","дама","король","туз"):
            deck.append(f"{card} {suit}")
    
    shuffle(deck)
    return deck


def get_card_points(card, dealer=False):
    received_card = card.split()
    card_points = {}

    for card in range(2,11):
        card_points[f'{card}'] = card
    for card in ("валет","дама","король"):
        card_points[f'{card}'] = 10
    if received_card[0] == "туз":
        if dealer:
            points = choice([1, 11])
        else:
            points = int(input('туз 1 или 11?\n'))
    else:
        points = card_points[received_card[0]]
    
    return points


your_points = 0
bot_points = 0
moves = 1

deck = get_deck()



def move(points, dealer=False):
    card = deck.pop()
    if dealer:
        card_point = get_card_points(card, dealer=True)
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

            

   