import random

def main():
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    Player_choose = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors"))

    Computer_choose = random.randint(0, 2)
    RPS = [rock, paper, scissors]
    if Player_choose <=2:
        print(f"You choose: {RPS[Player_choose]}")
        print(f"Computer choose: {RPS[Computer_choose]}")

        if Player_choose == 0 and Computer_choose == 2:
            print("You win!!!")
        elif Player_choose == 1 and Computer_choose == 0:
            print("You win!!!")
        elif Player_choose == 2 and Computer_choose == 1:
            print("You win!!!")
        elif Player_choose == Computer_choose:
            print("Draw")
        else:
            print("You lose :(")
    else:
        print("invalid input , only enter number between 0 - 2")
        
    restart = input("Do you want to play again?")
    if restart in ["yes","Yes"]:
        main()
    else:
        exit()
main()