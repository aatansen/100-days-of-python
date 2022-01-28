# way1:
def prime_checker(number):
    for i in range(2,number):
        if number%i==0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")
# way2:
def prime_checker2(number2):
    is_prime=True
    for i in range(2,number2):
        if number2%i==0:
            is_prime=False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_checker2(87)

# checking multiple prime number 
def prime_checkers(number2):
    is_prime=True
    for i in range(2,number2):
        if number2%i==0:
            is_prime=False
    if is_prime:
        print(number2)

for i in range(2,1001):
    prime_checkers(i)

