from calc_art import logo

def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2

operations = {"+":add , "-":subtract, "*":multiply, "/":divide}
def calculator():
    print(logo)
    n1 =float(input("\nWhats the first number?: "))
    should_continue = True
    while should_continue:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        n2 =float(input("Whats the next number?: "))
        result = operations[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {result} ")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if should_continue == "y":
            n1 = result
        elif should_continue == "n":
            should_continue = False
            print("\n"*20)
            calculator()
calculator()