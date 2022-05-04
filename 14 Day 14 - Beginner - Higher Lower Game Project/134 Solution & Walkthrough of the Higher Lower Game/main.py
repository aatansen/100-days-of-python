from operator import is_
import random
from art import logo, vs
from game_data import data
import os

# format the data
def format_data(acc):
    acc_name = acc['name']
    acc_des = acc['description']
    acc_country = acc['country']
    return f'{acc_name}, a {acc_des}, from {acc_country}'

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Display art
print(logo)
score = 0
game_continue = True
acc_b = random.choice(data)
# make the game repeatable
while game_continue:
    # Generate random data
    # changing position of data
    acc_a = acc_b
    acc_b = random.choice(data)
    while acc_a == acc_b:
        acc_b = random.choice(data)

    print(f'Compare A: {format_data(acc_a)}')
    print(acc_a['follower_count'])
    print(vs)
    print(f'Against B: {format_data(acc_b)}')
    print(acc_b['follower_count'])
    # # ask user to guese
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # # check if user is corrent
    a_follower_count = acc_a['follower_count']
    b_follower_count = acc_b['follower_count']
    # clear output every round
    os.system("cls")
    print(logo)
    # # get follower count
    is_corrent = check_answer(guess, a_follower_count, b_follower_count)
    # # give user feedback
    if is_corrent:
        print("You're right")
        score += 1
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_continue = False
