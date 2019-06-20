class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 1.5


x = Circle(20)
print(x.diameter)
print(x.radius)
print(x.diameter)
