# Calculator
from art import logo

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


def calculator():
    print(logo)
    num1 = float(input("What's the first number:"))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number:"))
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        choice = input(
            f"Type 'y' to continue with {answer} or type 'n' to start new calculation.")
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()