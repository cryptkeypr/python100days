import random

user_cards = []
npc_cards = []
is_game_over = False


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        print("Blackjack!")
        return 0
    elif total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return total


def replay():
    if input("[ ] Want to play again?  >> ") == "y":
        blackjack()
    else:
        quit()


def compare_score(user_score, npc_score):
    if user_score == npc_score:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "Draw"
    elif user_score == 0:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "You win!"
    elif npc_score == 0:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "Dealer wins."
    elif user_score > 21:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "You bust!"
    elif npc_score > 21:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "Dealer has bust, you win!"
    elif user_score > npc_score:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "You win!"
    else:
        print(f"Your score: {user_score}    Dealer score: {npc_score}")
        return "You lost."


def blackjack():
    want_to_play = input("Would you like to play Blackjack?    >> ").lower()
    if want_to_play != "y" and want_to_play != "n":
        print("Invalid answer, aborting..")
        quit()
    if want_to_play == "n":
        quit()

    for _ in range(2):
        user_cards.append(deal_card())
        npc_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        npc_score = calculate_score(npc_cards)
        print(f"\n    Your cards: {user_cards}    Your score: {user_score}")
        print(f"      Dealer's cards: {npc_cards[0]}")
        compare_score(user_score, npc_score)

        ask_to_draw = input("Would you like another card?  >> ").lower()
        if ask_to_draw == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            compare_score(user_score, npc_score)
        else:
            while npc_score < 17 and npc_score != 0:
                npc_cards.append(deal_card())
                npc_score = calculate_score(npc_cards)
                print(f"    Dealer's cards: {npc_cards} = {npc_score}")
            winner = compare_score(user_score, npc_score)
            print(winner)
            replay()


blackjack()

