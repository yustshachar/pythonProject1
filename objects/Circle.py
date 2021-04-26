

class Circle:
    def __init__(self, radius):
        self.radius=radius
        self.pi=3.14
    def area(self):
        shetah = self.radius
        # mekori = shetah
        for i in range(1, 2):
            shetah *= self.radius
        return self.pi*shetah
    def circumference(self):
        return self.radius*2*self.pi


radius=int(input("enter radius: "))
maagal=Circle(radius)
print(maagal.area())
print(maagal.circumference())