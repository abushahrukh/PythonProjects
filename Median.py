import numpy as np #Import the Module

def findmedian(number):
    sorted_numbers = np.sort(number)
    length = len(sorted_numbers)
    middle = length // 2
    
    if length % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2.0
    else:
        median = sorted_numbers[middle]
    
    return median

#input from the user
user_input = input("Enter numbers separated by spaces: \n")
number = np.array([int(x) for x in user_input.split()])

#Calculating the median
median = findmedian(number)

#Print median
print("Median:", median)
