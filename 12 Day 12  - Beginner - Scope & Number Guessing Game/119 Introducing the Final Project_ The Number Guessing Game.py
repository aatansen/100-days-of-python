import random
import os

logo = '''
   _____                       _______ _             _   _                 _               
  / ____|                     |__   __| |           | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___   |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/  | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___|  |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                                                                                                                                                                                             
'''
def game():
    print (logo)
    # Choosing a random number between 1 to 100
    c_guess = random.randint(1,100)
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 to 100')

    # creating a function to check
    def check_ans(u_guess,com_guess,turns):
        if com_guess > u_guess:
            print('Too low.')
            print('Guess again')
            return turns-1
        elif com_guess < u_guess:
            print('Too high.')
            print('Guess again')
            return turns-1
        else:
            print(f'Congratulation {user_guess} is correct, You Win !!!')

    # fuction to set difficulty 
    Easy_level =10
    Hard_level =5
    def set_difficulty():
        level = input("Choose a diifficulty. Type 'easy' or 'hard':")
        if level == 'hard':
            turns = Hard_level
        else:
            turns = Easy_level
        return turns
    turns = set_difficulty()


    user_guess =0
    while user_guess!=c_guess:
        print(f'You have {turns} attempts remaining to guess the number.' )
        # user guess 
        user_guess = int(input('Make a guess:'))

        turns = check_ans(user_guess,c_guess,turns)
        if turns ==0:
            print(f'You run out of guesses, Correct answer is: {c_guess}')
            return
game()
restart=input("wanna play again? 'yes' or 'no'").lower()
if restart=="yes":
    os.system("cls")
    game()
else:
    exit()
