import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def smallest_evenly_divisible(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

# Find the smallest number divisible by all numbers from 1 to 20
smallest_number = smallest_evenly_divisible(20)
print("Smallest number divisible by all numbers from 1 to 20:", smallest_number)
