# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
print("Welcome to the secret auction program.")

auction_dict = {}

other_bidders = True
while other_bidders:
    name = input("What is your name? \n")
    bid = int(input("What's your bid? \n"))
    auction_dict[name] = bid
    answer = input("Are they any other bidders? Type 'yes' or 'no'. \n").lower()
    print("\n" * 100)
    if answer != "yes":
        break

highest_price = 0
winner_name = ""
for n in auction_dict:
    if auction_dict[n] > highest_price:
        highest_price = auction_dict[n]
        winner_name = n
print(f"The winner is {winner_name} with a bid of ${highest_price}")