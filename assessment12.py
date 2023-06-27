class Rectangle:
    def __init__(self):
        self.width = 120
        self.height = 100.5

    def area(self):
        return self.width*self.height(float)
    def perimeter(self):
        return 2*self.width + 2*self.height(float)
    def scale(self, n):
        self.height *= n
        self.width *= n

rectangle = Rectangle()
area= rectangle.area()
perimeter= rectangle.perimeter()
print(area)
print(perimeter)