# Exercise #1
# Write a Python class named Rectangle constructed by a length and width and a method that will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


a = int(input("Enter length of rectangle: "))
b = int(input("Enter width of rectangle: "))
obj = Rectangle(a, b)
print("Area of rectangle:", obj.area())

