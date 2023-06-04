import random
roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print("Rolling the dice...")
    print("The values are...")
    print(random.randint(1, 6))
    print(random.randint(1, 6))

    roll_again = raw_input("Roll the dice again? (yes/no): \n")
