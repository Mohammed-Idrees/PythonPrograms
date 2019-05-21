import abc
from abc import ABC, abstractmethod


class R(ABC):
    @abc.abstractproperty
    def rk(self):
        print("Abstract Base Class")


class K(R):
    @property
    def rk(self):
        super().rk()
        print("subclass ")

    # Driver code


r = K()
r.rk()