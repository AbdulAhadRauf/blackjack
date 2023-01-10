import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if score == 21 and len(cards) > 2 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    else:
        return score


def compare(pc_score, user_score):
    if pc_score == user_score:
        return "draw"
    elif pc_score == 0:
        return "Pc has black jack"
    elif user_score == 0:
        return "You have black jack"
    elif user_score > 21:
        return "You loose you > 21 "
    elif pc_score > 21:
        return "You win pc > 21"
    elif pc_score < user_score:
        return "You Win"
    else:
        return "You Loose"


def play_game():
    game_over = False

    user = []
    pc = []

    for i in range(2):
        user.append(deal_card())
        pc.append(deal_card())

    while not game_over:
        user_score = calculate_score(user)
        pc_score = calculate_score(pc)
        print(f'You: {user}, Total: {user_score}')
        print(f'pc: {pc[0]}')
        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True
        else:
            direction = input("do you want to continue? y/n").lower()
            if direction == "y":
                user.append(deal_card())
                game_over = False
            else:
                game_over = True

    while pc_score != 0 and pc_score <= 17:
        pc.append(deal_card())
        pc_score = calculate_score(pc)
    print(f"   Your final hand: {user}, final score: {user_score}")
    print(f"   Computer's final hand: {pc}, final score: {pc_score}")
    print(compare(pc_score, user_score))


while input('Do you want to play a game of black jack? y/n').lower() == "y":
    clear()
    play_game()
