# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
if position == "00":
    map[0][0]="X"
elif position == "01":
    map[0][1]="X"
elif position == "02":
    map[0][2]="X"   
elif position == "10":
    map[1][0]="X"
elif position == "11":
    map[1][1]="X"
elif position == "00":
    map[0][0]="X"
elif position == "12":
    map[1][2]="X"
elif position == "21":
    map[2][1]="X"
else:
    map[2][2]="X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")