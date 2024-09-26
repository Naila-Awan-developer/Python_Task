### Tringle Task ##
import math
class Point: #Class to represent a point in 2D space.
    def __init__(self, x, y):#Initialize Point object
        self.__x = x
        self.__y = y

    def __str__(self):#Return string representation of Point object.
        return f"({self.__x}, {self.__y})"
    def distance_from(self, other): #Calculate distance between two points.
        return math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
class Triangle: #Class to represent a triangle defined by three points.
    def __init__(self, p1, p2, p3): #Initialize Triangle object.
        self.__points = [p1, p2, p3]
    def perimeter(self):#Calculate perimeter of the triangle.
        perimeter = 0
        for i in range(3):
            perimeter += self.__points[i].distance_from(self.__points[(i+1)%3])
        return perimeter

p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(6, 0)
triangle = Triangle(p1, p2, p3)
print(f"Perimeter: {triangle.perimeter()}")