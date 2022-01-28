import random
word_list = ['ardvark', 'baboon', 'camel', 'apple']
chosen_word = random.choice(word_list)

chosen_word = 'apple'
# guess="p"

chosen_word_list = list(chosen_word)
print(chosen_word_list)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()
lives=len(stages)
# print(lives)

spaces_len = len(chosen_word)
spaces_list = []
for i in range(spaces_len):
    spaces = spaces_list.append("_")
# print(spaces_list)
end_game = False
while not end_game:
    guess = input("Guess a letter:")
    for i in range(spaces_len):
        if chosen_word_list[i] == guess:
            spaces_list[i] = guess
            

    if guess not in chosen_word_list:
      lives-=1

      if lives==0:
        end_game=True
        
        print("You lose")

    print(f"{' '.join(spaces_list)}")
    if "_" not in spaces_list:
        end_game = True
        print("You Win!!")
    print(stages[lives])