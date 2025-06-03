import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
decision = 'n'

while decision == 'n':
    n1 = int(input("What's the first number?: "))
    print(" + \n - \n * \n /")
    operation_symbol = input("Pick an operation: ")
    n2 = int(input("What's the second number?: "))

    decision = 'y'
    while decision == 'y':
        def first_op():
            return operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {first_op()}")
        decision = input(f"Type 'y' to continue calculating with {first_op()} or type 'n' to start a new calculation: ")
        if decision == 'y':
            n1 = first_op()
            print(" + \n - \n * \n /")
            operation_symbol = input("Pick an operation: ")
            n2 = int(input("What's the next number?: "))
        else:
            print("\n " * 10)
            print(art.logo)