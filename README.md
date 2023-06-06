<div align="center">
<h1>100 days of Python</h1>
</div>

</br>
<details>
<summary>Extra Notes</summary>

## Notes

### 01 Prime Number

Way 01

```python
def prime_checker(number):
    for i in range(2,number):
        if number%i==0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")
```

Way 02

```python
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
```

Checking multiple prime number 

```python
def prime_checkers(number2):
    is_prime=True
    for i in range(2,number2):
        if number2%i==0:
            is_prime=False
    if is_prime:
        print(number2)

for i in range(2,1001):
    prime_checkers(i)
```

### 02 Time Calculation

Current time

```python
import datetime
current_date_and_time = datetime.datetime.now()
print(current_date_and_time)
# OUTPUT
# 2020-03-27 19:01:31.340242
```

Future time calculation

```python
hours_added = datetime.timedelta(hours = 9,minutes=40)

future_date_and_time = current_date_and_time + hours_added

print(future_date_and_time)
# OUTPUT
# 2020-03-28 00:01:31.340242
```

Time subtraction

```python
from datetime import datetime
past_date = '28/02/22 13:27:19'
past_date = datetime.strptime(past_date, '%d/%m/%y %H:%M:%S')
current_date = '13/03/22 18:06:19'
current_date = datetime.strptime(current_date, '%d/%m/%y %H:%M:%S')

print (current_date-past_date)
# Feb 28, 2022, 1:27 PM
```

### 03 Calculate Leap Year

01 Write a program that prints the next 20 leap years starting from the leap year closest to what the user enters

```python
year = int(input("Enter a year:"))
for yr in range (year,year+80):
    if yr%400==0:
        print("Leap Year.")
    elif yr%100==0:
        print("Not Leap Year.")
    elif yr%4==0:
        print("Leap Year.")
    else:
        print("Not leap year.")
```

### 04 COCOMO Model

```python
# Function to calculate parameters of Basic COCOMO
def calculate(table ,mode ,size):
    effort = 0
    time = 0
    staff = 0
    model = 0
     
    # Check the mode according to size
    if(size >= 2 and size <= 50):
        model = 0
    elif(size > 50 and size <= 300):
        model = 1
    elif(size > 300):
        model = 2
     
    print(f"The mode is {mode[model]}")
     
    # Calculate Effort
    effort = table[model][0]*pow(size, table[model][1])
     
    # Calculate Time
    time = table[model][2]*pow(effort, table[model][3])
     
    #Calculate Persons Required
    staff = (effort/time)
     
    # Output the values calculated
    print(f"Effort = {round(effort,3)} Person-Month")
    print(f"Development Time = {round(time,3)} Months")
    print(f"Average Staff Required = {round(staff)} Persons")
 
table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
mode = ["Organic","Semi-Detached","Embedded"]
size = int(input("Enter KLOC Size:"))
calculate(table, mode, size)
```

### 05 Print list as a normal string

```
list_name = ["hello","world"]
# print list as a normal string:
print(f"{' '.join(list_name)}")
```

### 06 Clear output

```python
import os
os.system("cls")
```

### 07 Understanding Caesar Cipher

```python
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_or="cay"
word=list(word_or)
# print(word)
# x=alphabet.index('c')
# print(x)
shift=5

encrypt_word=""
for i in range(len(word)):
    word_by_word=word[i]
    encrypt_letter=alphabet.index(word_by_word)+shift
    # print(encrypt_letter)
    if encrypt_letter>=26:
        # fixing index error
        index_sol=encrypt_letter-len(alphabet)
        encrypt_word+=alphabet[index_sol]
    else:
        encrypt_word+=alphabet[encrypt_letter]
print(f"original word is: {word_or}")
print(f"encrypted word is: {encrypt_word}")
```

### 08 Rerun program

```python
# rerun the program using function:
def main():
    num=int(input("enter a number:"))
    print(f"Your entered number is {num}.")

    restart=input("Enter number again? 'yes' or 'no'").lower()
    if restart=="yes":
        main()
    else:
        exit()
main()

# rerun the program using condition 'while':
is_restart=True
while is_restart:
    num=int(input("enter a number:"))
    print(f"Your entered number is {num}.")
    restart=input("Enter number again? 'yes' or 'no'").lower()
    if restart=="no":
        is_restart=False
```

### 09 Recursion concept

```python
# day 10 104 learning on calculator recursion
def calculator():
    # Add
    def add(n1, n2):
        return n1+n2
    operations = {
        '+': add,
    }

    num1 = int(input("What's the first number:"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number:"))
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        choice = input(
            f"Type 'y' to continue with {answer} or type 'n' to start new calculation.")
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() # recursion

calculator()
```

### 10 Randomly choice from a list

```python
# from day 11: 109
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
x=deal_card()
print(x)
```

### 11 Modify global variable

Way 01

```python
# from day 12 : 117
enemies = 1
def increase_enemies():
    global enemies
    enemies+=1
    print(f'enemies inside function: {enemies}')
increase_enemies()
print(f'enemies outside function: {enemies}')
```

Way 02

```python
foe = 1
def increase_enemies():
    return foe+1

foe = increase_enemies()
print(f'enemies outside function: {enemies}')
```

### 12 Randomly get data

```python
# note from day 14:
import random
data = [1,2,4,5] # eample data ..main data is in list of key values
acc_a = random.choice(data)
acc_b = random.choice(data)
if acc_a == acc_b:
    acc_b = random.choice(data)

#format the data 
def format_data(acc):
    acc_name = acc['name']
    acc_des = acc['description']
    acc_country = acc['country']
    return f'{acc_name}, a {acc_des}, from {acc_country}'

print(f'Compare A: {format_data(acc_a)}')
print(acc_a['follower_count'])
print('vs')
print(f'Compare B: {format_data(acc_b)}')
print(acc_b['follower_count'])
```

</details>