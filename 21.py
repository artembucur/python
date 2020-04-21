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
        if dealer == True:
            points = choice([1, 11])
        else:
            points = int(input('туз 1 или 11?\n'))
    else:
        points = card_points[received_card[0]]
    
    return points


def go(points, dealer=False):

    try:
        card = deck.pop()
    except:
        print("В колоде закончились карты")
        sleep(4)
        exit()

    if dealer:
        card_point = get_card_points(card, dealer=True)
    else:
        card_point = get_card_points(card)
    
    points += card_point

    print(f'''
    Вам выпало: {card}
    Очки: {points}
    ''') 
    return points


deck = get_deck()

play_again = "да"
while play_again == 'да':

    your_points = 0
    bot_points = 0
    more = 'да'
    move = 1

    while more == "да":
        
        if move == 1:
            print("Ход бота:")
            bot_points = go(bot_points, True)

            for _ in range(2):
                print("Ваш ход:")
                your_points = go(your_points)
                sleep(2)
        else:
            print("Ваш ход:")
            your_points = go(your_points)
            sleep(2)
        
        if your_points > 21:
            print("Вы проиграли")
            break
        elif your_points == 21:
            print("Black Jack!!!")
            more = "нет"
        else:
            more = input("Вытянуть карту ещё? да или нет\n")    
        move += 1
    else:
            
        while bot_points < 18:
            print("Ход бота:")
            bot_points = go(bot_points, True)

        if bot_points > 21:
            print("Вы выиграли")

        elif bot_points == your_points:
            print("Ничья")
        elif your_points < bot_points:
            print("Вы проиграли")
    
    

    play_again = input("Играем ещё?\n")

            

   