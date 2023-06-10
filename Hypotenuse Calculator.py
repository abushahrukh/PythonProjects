def pythagoras_theorem(x,y):  #Pythagoras Theorem Formula
    z = (((x**2) +  (y**2))**0.5)
    return z

x = int(input("Enter your Base/Adjacent Side\n" ))
y = int(input("Enter your Perpendicular/Opposite Side\n"))
print("Your Hypotenuse is  " + str(pythagoras_theorem(x,y)))