from art import logo

def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("[Number 1]:   "))

  still_calculating = True
  while still_calculating:
    chosen_symbol = input("Choose an operator: ")
    num2 = float(input("[Number 2]:   "))
    calc_function = operations[chosen_symbol]
    answer = calc_function(num1, num2)

    print(f"\n[[{num1} {chosen_symbol} {num2} = {answer}]]\n")
    
    go_again = input(f"-- Would you like to continue with [{answer}] - ['Y']\n-- Start a new calculation - ['N']\n-- Or quit - ['Q']?:\n>> ").lower()
    if go_again == "q":
       still_calculating = False
    elif go_again == "y":
        num1 = answer
    elif go_again == "n":
      go_again = False
      calculator()


calculator()
