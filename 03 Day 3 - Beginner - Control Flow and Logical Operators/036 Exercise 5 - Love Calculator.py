# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
com_name = (name1+name2).lower()
t_count = com_name.count("t")
r_count = com_name.count("r")
u_count = com_name.count("u")
e_count = com_name.count("e")
l_count = com_name.count("l")
o_count = com_name.count("o")
v_count = com_name.count("v")
e_count = com_name.count("e")
true = str(t_count+r_count+u_count+e_count)
love = str(l_count+o_count+v_count+e_count)
true_love = int(true+love)
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
