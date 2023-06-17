def is_power_of_five(num):
    if num <= 0:
        return False
    while num % 5 == 0:
        num //= 5
    return num == 1


num = int(input("Enter a positive integer: \n"))


if is_power_of_five(num):
    print(num, "is a power of five")
else:
    print(num, "is not a power of five")
