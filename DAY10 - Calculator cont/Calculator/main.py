from art import logo


# function to add two numbers
def add(first_number, second_number):
    return first_number + second_number


# function to subtract two numbers
def subtract(first_number, second_number):
    return first_number - second_number


# function to multiply two numbers
def multiply(first_number, second_number):
    return first_number * second_number


# function to divide two numbers
def divide(first_number, second_number):
    return first_number / second_number


# dictionary to store operations
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }


def calculator():
    print(logo)
    keep_calculating = True
    number1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)
    operation = input("Pick an operation from the line above: ")

    number2 = float(input("What's the next number?: "))

    for key, value in operations.items():
        if key == operation:
            result = value(number1, number2)

    print(f"{number1} {operation} {number2} = {result}")

    repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if repeat != 'y':
        calculator()

    while keep_calculating:
        operation = input("Pick an operation:")
        number2 = float(input("What's the next number?: "))
        number1 = result

        for key, value in operations.items():
            if key == operation:
                result = value(number1, number2)

        print(f"{number1} {operation} {number2} = {result}")
        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if repeat == 'y':
            continue
        elif repeat == 'n':
            del number1, number2, result
            calculator()


calculator()
