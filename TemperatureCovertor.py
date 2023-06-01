def Celcius_to_Fahrenheit(c):
    formula = (c * 1.8) + 32
    return formula

def Fahrenheit_to_Celsius(f):
    formula = (f - 32) * (5/9)
    return formula

x = input("Celcius or Fahrenheit?\n")
if x.lower() == "celcius" or x.lower() == "c":
    z = float(input("Enter value in Celsius: "))
    print("Converted temperature in Fahrenheit:", Celcius_to_Fahrenheit(z))
elif x.lower() == "fahrenheit" or x.lower() == "f":
    z = float(input("Enter value in Fahrenheit: "))
    print("Converted temperature in Celsius:", Fahrenheit_to_Celsius(z))
else:
    print("Invalid input")

