a = 0
b = 1

while a <= 100000000:
    if a % 2 == 0:
        print(a)
    a, b = b, a + b
