def main():
    calc()


def opr():
    print("+")
    print("-")
    print("*")
    print("/")
    choice = input("Pick an operation: ")
    return choice


def calc(first=None):  # need to make calc recursive, so it should call itself at some point.
    operations = {      # This means all logic should be here.
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Cannot divide by 0"
    }

    if first is None:
        first = int(input("Please enter the first number: "))

    operator = opr()
    second = int(input("Please enter the second number:"))
    operation = operations.get(operator)
    if operation:
        answer = operation(first, second)
        print(f"Result: {first} {operator} {second} = {answer}")
        if isinstance(answer, str):
            return
        c = input(f"Press 'y' to continue calculating with {answer}, or press 'n' to start a new calculation.")
        if c == 'y':
            calc(answer)
        else:
            calc()
    else:
        print("Invalid operator.")
        calc()


main()
