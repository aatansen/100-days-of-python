# Calculator

# Add
def add(n1, n2):
    return n1+n2

# Sub


def sub(n1, n2):
    return n1-n2

# Mul


def mul(n1, n2):
    return n1*n2

# Div


def div(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

num1 = int(input("What's the first number:"))
num2 = int(input("What's the second number:"))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

calculate = operations[operation_symbol]
answer = calculate(num1,num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')