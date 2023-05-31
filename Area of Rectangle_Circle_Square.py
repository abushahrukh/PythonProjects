import math

def rectangle_area(length, width):
    area = length * width #Area length multiply by width
    return area

def circle_area(radius):
    area = math.pi * radius**2 # Area Pi into R squared
    return area

def square_area(side):
    area = side**2 # length squared
    return area

def main():
    shape = input("Choose a shape (rectangle, circle, square): ")

    if shape == "rectangle" or "Rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
    elif shape == "circle" or "Circle":
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
    elif shape == "square" or "Squared ":
        side = float(input("Enter the length of the side of the square: "))
        area = square_area(side)
    else:
        print("Spelling Mistake Or Invalid/Wrong Shape")
        return

    print("Area:", area)

if __name__ == "__main__":
    main()
