#Write your code below this line 👇
def prime_checker(number):
    for i in range(2,number):
        if number%i==0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.