from ICalcGeo import ICalcGeo
import math


class Cercle(ICalcGeo):

    def __init__(self, rayon=0) -> None:
        print("init Cercle")
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon
    
    @rayon.setter
    def rayon(self,value):
        self._rayon = value

    def get_surface(self):
        return math.pi*self._rayon**2

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._rayon=}"