import os
from art import logo


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("Type a number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        flag = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to exit the calculation: "
        )

        if flag == "y":
            num1 = answer
        elif flag == "n":
            should_continue = False
            clear()
            calculator()
        elif flag == "exit":
            clear()
            should_continue = False
        else:
            clear()
            print("Wrong input. Please Select correct operation")
            should_continue = False


calculator()
