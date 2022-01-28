import random
from hangman_art import *
from hangman_wordlist import *
import os
chosen_word = random.choice(word_list)

# chosen_word = 'apple'
# guess="p"
print(f"Chosen word is {chosen_word}")
chosen_word_list = list(chosen_word)

stages.reverse()
lives=6
# print(lives)

spaces_len = len(chosen_word)
spaces_list = []
for i in range(spaces_len):
    spaces = spaces_list.append("_")
# print(spaces_list)
end_game = False
print(logo)
while not end_game:
    
    guess = input("Guess a letter:")
    
    os.system("cls")
    # telling the user that he already guess this letter:          
    if guess in spaces_list:
        print(f"You already guess {guess}")
    for i in range(spaces_len):
        if chosen_word_list[i] == guess:
            spaces_list[i] = guess



# lives down if user guess wrong letter:    
    if guess not in chosen_word_list:
      lives-=1
      print("Opps wrong letter.")
      if lives==0:
        end_game=True
        
        print("You lose")

# showing the user guesses result:
    print(f"{' '.join(spaces_list)}")
# checking how many guess left :
    if "_" not in spaces_list:
        end_game = True
        print("You Win!!")
    print(stages[lives])
