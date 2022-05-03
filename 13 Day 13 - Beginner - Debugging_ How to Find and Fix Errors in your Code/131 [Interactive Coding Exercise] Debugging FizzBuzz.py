for number in range(1, 101):
    print(f'current number is: {number}') # printing number for detail debugging
    if number % 3 == 0 and number % 5 == 0: # changed or to and 
        print("FizzBuzz")
    elif number % 3 == 0: # added elif
        print("Fizz")
    elif number % 5 == 0: # added elif
        print("Buzz")
    else:
        print(number) # remove []