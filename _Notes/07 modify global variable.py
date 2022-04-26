# from day 12 : 117
# way 1:
enemies = 1
def increase_enemies():
    global enemies
    enemies+=1
    print(f'enemies inside function: {enemies}')
increase_enemies()
print(f'enemies outside function: {enemies}')

# way 2:

foe = 1
def increase_enemies():
    return foe+1

foe = increase_enemies()
print(f'enemies outside function: {enemies}')
