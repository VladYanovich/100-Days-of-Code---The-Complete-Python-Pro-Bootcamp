import random
import art
import game_data

A = random.choice(game_data.data)
B = random.choice(game_data.data)
higher_lower = True
current_score = 0
print(art.logo)
while higher_lower:
    if current_score != 0:
        print(f"You're right! Current Score: {current_score}")
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    print(art.vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    user_output = input("Who has more followers? Type 'A' or 'B': ").upper()
    if A['follower_count'] > B['follower_count'] and user_output == 'A':
        print("\n" * 10)
        current_score += 1
        print(art.logo)
        print(f"{A["name"]}, a {A["description"]}, from {A["country"]}, has {A['follower_count']}MLN Subscribers")
        print(f"{B["name"]}, a {B["description"]}, from {B["country"]}, has {B['follower_count']}MLN Subscribers")
    elif A['follower_count'] < B['follower_count'] and user_output == 'B':
        print("\n" * 10)
        current_score += 1
        print(art.logo)
        print(f"{A["name"]}, a {A["description"]}, from {A["country"]}, has {A['follower_count']}MLN Subscribers")
        print(f"{B["name"]}, a {B["description"]}, from {B["country"]}, has {B['follower_count']}MLN Subscribers")
    else:
        break
    A = B
    B = random.choice(game_data.data)
print("\n" * 30)
print(f"{A["name"]}, a {A["description"]}, from {A["country"]}, has {A['follower_count']}MLN Subscribers")
print(f"{B["name"]}, a {B["description"]}, from {B["country"]}, has {B['follower_count']}MLN Subscribers")
print(f"Sorry, that's wrong! Current Score: {current_score}")