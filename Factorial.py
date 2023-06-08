def factorial_counter(n):  #Factorial Module50
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

# user input
num = int(input("Enter a number: \n"))

# Calculate the factorial
result = factorial_counter(num)

# Display the result
print("The factorial of", num, "is", result)
