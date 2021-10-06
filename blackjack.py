
import random
# ace is 11 unless over 21
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []
player_score = sum(player_cards)
computer_score = sum(computer_cards)
replays = 0


def replay(answer):
    if answer.lower() == "y":
        blackjack()
    else:
        quit()
        return 0


def check_score(player):
    if player == player_score:
        if player_score == 21:
            print(f"{player_cards} = {player_score}")
            print("You win!")
            replay(answer=input("Play again? 'y' or 'n': "))
            return 0
        elif player_score > 21:
            print(f"{player_cards} = {player_score}")
            print("You bust.")
            replay(answer=input("Play again? 'y' or 'n': "))
    elif player == computer_score:
        if computer_score == 21:
            print(f"{computer_cards} = {computer_score}")
            print("Computer wins.")
            replay(answer=input("Play again? 'y' or 'n': "))
        elif computer_score > 21:
            print(f"{computer_cards} = {computer_score}")
            print("Computer bust.")
            replay(answer=input("Play again? 'y' or 'n': "))
        elif computer_score == 17:
            print("The computer wont draw, it is at 17.")
        elif computer_score > 17:
            print("The computer wont draw, it is above 17.")


def draw_card(user):
    if user == "player":
        card = player_cards.append(random.choice(cards))
        # add player score??
        check_score(player_score)
    elif user == "computer":
        if player_score < 17:
            card = computer_cards.append(random.choice(cards))
            # add computer score??
            check_score(computer_score)


def blackjack():
    print("##########BLACKJACK##########")
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    draw_card("player")
    draw_card("player")
    check_score(player_score)
    draw_card("computer")
    draw_card("computer")
    check_score(computer_score)
    playing = True
    while playing:
        print(f"Your cards: {player_cards} SCORE [{player_score}]")
        print(f"Computer's cards: {computer_cards} SCORE [{computer_score}]")
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == "y":
            print("HIT!")
            draw_card("player")
            check_score(player_score)
            if computer_score < 17:
                draw_card("computer")
                check_score(computer_score)
            else:
                blackjack()
        elif draw == "n":
            playing = False


blackjack()

