def findcommondivisors(a, b):
    divisors_a = finddivisors(a)
    divisors_b = finddivisors(b)
    commondivisors = divisors_a.intersection(divisors_b)
    return commondivisors

def finddivisors(num):
    divisors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.add(i)
    return divisors


num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

commondivisors = findcommondivisors(num1, num2)
print("Common divisors:", commondivisors)
