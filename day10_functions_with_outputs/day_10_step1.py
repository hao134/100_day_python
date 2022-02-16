from art import logo

def add(a1, a2):
  return a1 + a2

def subtract(a1, a2):
  return a1 - a2

def multiply(a1, a2):
  return a1 * a2

def divide(a1, a2):
  return a1 / a2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()