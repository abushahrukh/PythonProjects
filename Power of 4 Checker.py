def is_power_of_four(num):
    if num <= 0:
        return False
    while num % 4 == 0:
        num //= 4
    return num == 1


num = int(input("Enter a positive integer: "))


if is_power_of_four(num):
    print(num, "is a power of four")
else:
    print(num, "is not a power of four")
