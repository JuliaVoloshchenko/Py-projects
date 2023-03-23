'''
Реализовать дескрипторы для любых двух классов
'''


class NonNegative:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value


class Road:
    length = NonNegative('length')
    width = NonNegative('width')
    mass = 25
    thickness = 0.05

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_calculation(self, mass, thickness):
        res = self.length * self.width * mass * thickness
        return res


obj = Road(5000, -20)
print(obj.mass_calculation(25, 0.05))
