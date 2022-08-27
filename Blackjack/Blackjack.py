import random
from art import logo


def check_score(deck: list) -> (list, int):
    if sum(deck) > 21 and 11 in deck:
        deck[deck.index(11)] = 1
    return deck, sum(deck)


def one_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_deck, computer_score = check_score(random.choices(cards, k=2))
    user_deck, user_score = check_score(random.choices(cards, k=2))

    print(f"Your deck: {user_deck}, score = {user_score}")
    print(f"Computer's first card: {computer_deck[0]}")

    if user_score == 21 and computer_score != 21:
        return "won"
    elif user_score != 21 and computer_score == 21:
        print(f"Computer's deck: {computer_deck}")
        return "lost"
    elif user_score == 21 and computer_score == 21:
        print(f"Computer's deck: {computer_deck}")
        return "draw"

    add_card = "y"
    while add_card == "y" and user_score <= 21:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while add_card != "y" and add_card != "n":
            # while not (add_card == "y" or add_card == "n"):
            add_card = input("Invalid input. Type 'y' to get another card, type 'n' to pass: ").lower()
        if add_card == "y":
            user_deck.append(random.choice(cards))
            user_deck, user_score = check_score(user_deck)
            print(f"Your deck: {user_deck}, score = {user_score}")

    if user_score > 21:
        print("Bust")
        return "lost"

    print(f"Computer's deck: {computer_deck}, score = {computer_score}")

    while computer_score <= 16:
        computer_deck.append(random.choice(cards))
        computer_deck, computer_score = check_score(computer_deck)
        print(f"Computer's deck: {computer_deck}, score = {computer_score}")
        if computer_score > 21:
            print("Bust")
            return "won"

    if user_score > computer_score:
        return "won"
    elif user_score < computer_score:
        return "lost"
    else:
        return "draw"


play_again = 'y'

while play_again == 'y':

    print(logo)
    game_state = one_game()
    sentence = f"You {game_state} this round." if game_state in ("won", "lost") else "This round is a draw."

    play_again = input((f"{sentence} Would you want another round? y/n: ").lower())

    while play_again != "y" and play_again != "n":
        play_again = input((f"Invalid input. Would you want another round? y/n: ").lower())



print("Thank you for playing!")
