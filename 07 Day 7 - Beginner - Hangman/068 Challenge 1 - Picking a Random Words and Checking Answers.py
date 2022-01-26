import random
word_list = ['ardvark','baboon','camel']
chosen_word=random.choice(word_list)
guess=input("Guess a letter:")
guess=guess.lower()
print(guess)
find_word=chosen_word.find('a')
for check in chosen_word:
    if check==guess:
        print("Right")
    else:
        print("Wrong")
print(f"Chosen word was:{chosen_word}")


