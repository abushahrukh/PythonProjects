import random
digits = [0,1,2,3,4,5,6,7,8,9]
for i in range (10):
    threedigits = random.sample(digits, 3)
    number = int(''.join(map(str, threedigits)))
    print(number)