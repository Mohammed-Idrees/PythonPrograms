import abc
from abc import ABC, abstractmethod

class Polygon(ABC):
    '''Polygon Class'''
    # abstract method
    @abc.abstractproperty
    def noofsides(self):
        pass
    def printHello(self):
        print("hello")

    def sayHello(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    # Driver code

#a = Polygon()
R = Triangle()
R.noofsides()
R.printHello()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

print(Polygon.__doc__)