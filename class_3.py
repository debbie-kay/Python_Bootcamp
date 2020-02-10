class Circles():
    pi = 3.14
    def __init__(self,radius):
        self.rad = radius
    def area(self):
        return self.pi*self.rad**2
    def circumference(self):
        return 2*self.pi*self.rad
circle1 = Circles(radius = 24)
circle2 = Circles(radius = 23)
circle1.circumference()
circle1.area()
circle2.area()
circle2.circumference()
