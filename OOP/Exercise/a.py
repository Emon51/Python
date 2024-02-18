#Problem: Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416
    
    def area(self):
        return (self.pi * self.radius**2)
    
    def perimeter(self):
        return (2 * self.pi * self.radius)
#=================================================================================================


radius = float(input("Input the radius of the circle: "))

circle1 = Circle(radius)

area = circle1.area()
perimeter = circle1.perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 

