from art import CalculatorLogo
print(CalculatorLogo)

# Calculator Functiona

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary of Calc Functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_continue = True

num1 = float(input("What is the first number?\n"))
while should_continue:
    for symbol in operations:
        print(symbol)
    operation_chosen = input("Pick a symbol from the symbols above.\n")
    num2 = float(input("What is the next number?\n"))
    answer = operations[operation_chosen](num1, num2)
    print(f"{num1} {operation_chosen} {num2} = {answer}")
    continue_calculating = input(f"If you would like to continue with {answer} type 'Y' else "
                                 f"type 'N'\n").upper()
    if continue_calculating == 'N':
        should_continue = False
    num1 = answer
