for number in range(10001):
    if number % 3 == 0 and number % 5 == 0:
        print(number, "is divisible by both 3 and 5")
    elif number % 3 == 0:
        print(number, "is divisible by 3")
    elif number % 5 == 0:
        print(number, "is divisible by 5")
    else:
        print(number, "is indivisible by both 3 and 5")
