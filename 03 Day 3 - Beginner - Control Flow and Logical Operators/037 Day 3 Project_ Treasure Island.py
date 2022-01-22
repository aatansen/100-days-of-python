print("Welcome to Tresure Island.\nYour mission is to find the treasure.")
choose1=(input("type 'left' or 'right' ")).lower()
if choose1 == 'right':
    print("Game Over.")
else:
    choose2 = (input("type 'swim' or 'wait'")).lower()
    if choose2=='swim':
        print("Game Over.")
    else:
        choose3 = (input("type 'red' 'blue' or 'yellow'")).lower()
        if choose3=='red' or choose3 == 'blue':
            print("Game Over")
        else:
            print("You Win!")