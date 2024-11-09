import math



class shape:

    def area(self):
        raise NotImplementedError

class rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width* self.height

class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius):
        return math.pi * radius ** 2
    def print_area(shape):
        print('the area is',shape.area())

    rectangle=rectangle(5,3)
    circle=circle(4)
    

