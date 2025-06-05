import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wanna_play = input("Do you want to play a game Blackjack? Type 'y' or 'n': ")
while wanna_play == 'y':
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    if sum(your_cards) > 11 and 11 in your_cards:
        your_cards[your_cards.index(11)] = 1
    def printing(final):
        if final == "no":
            print(f"    Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"    Computer's first card: {computer_cards[0]}")
        else:
            print(f"   Your final hand: {your_cards}, final score: {sum(your_cards)}")
            print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    print(art.logo)
    printing(final = "no")
    wanna_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while wanna_card == 'y' and sum(your_cards) != 21:
        your_cards.append(random.choice(cards))
        if sum(your_cards) > 11 and  11 in your_cards:
            your_cards[your_cards.index(11)] = 1
        printing(final="no")
        if sum(your_cards) > 21:
            break
        wanna_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if sum(your_cards) > 21:
        printing(final="no")
        print("You went over. You lose")
    else:
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        if sum(your_cards) == sum(computer_cards):
            printing(final="yes")
            print("Draw")
        elif sum(your_cards) > sum(computer_cards) and sum(computer_cards) < 22:
            printing(final="yes")
            print("You win")
        elif sum(your_cards) < sum(computer_cards) and sum(computer_cards) < 22:
            printing(final="yes")
            print("You lose")
        else:
            printing(final="yes")
            print("You win")

    wanna_play = input("Do you want to play a game Blackjack? Type 'y' or 'n': ")