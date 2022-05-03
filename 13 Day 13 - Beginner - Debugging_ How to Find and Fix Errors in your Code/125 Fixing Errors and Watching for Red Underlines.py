############DEBUGGING#####################

# Fix the Errors
age = int(input("How old are you?")) # added int to make the string to int
if age > 18:
    print(f"You can drive at age {age}.") # added f string
# added else statement if the age is lower equal to 18
else:
    print(f"You can't drive at age {age}.")
