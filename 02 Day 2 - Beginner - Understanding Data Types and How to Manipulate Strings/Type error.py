num = 5
# print("number is"+num) #error because of concating string and integer

# right way:
print("number is", num)
print(f"number is {num}")  # best way

# bad way:
str_num = str(num)
print("Number is "+str_num)
