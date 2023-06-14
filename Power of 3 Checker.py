def is_power_of_three(num):
    if num <= 0:
        return False
    while num % 3 == 0:
        num //= 3
    return num == 1


num = int(input("Enter a positive integer: "))


if is_power_of_three(num):
    print(num, "is a power of three")
else:
    print(num, "is not a power of three")
