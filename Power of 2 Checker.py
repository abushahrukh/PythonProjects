def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0  #Using BitWise Operator


num = int(input("Enter a positive integer: "))
if is_power_of_two(num):
    print(num, "is a power of two.")
else:
    print(num, "is not a power of two.")
