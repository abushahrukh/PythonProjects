def add(num1, num2):   #For Addition
    return num1 + num2

def subtract(num1, num2): #For Substraction
    return num1 - num2

def multiply(num1, num2): #For Multipication
    return num1 * num2

def divide(num1, num2):  #For Division
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def calculator():
    print("Welcome to the Basic Calculator!")
    num1 = float(input("Enter the first number: \n"))
    num2 = float(input("Enter the second number: \n"))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): \n")

    if choice == '1':
        result = add(num1, num2)
        print("Result After Addition: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result After Substraction: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result After Multipication: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result After Division: ", result)
    else:
        print("Invalid choice. Please try again.")

calculator()
