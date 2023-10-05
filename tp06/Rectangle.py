


from typing import Any


class Rectangle:

    _cpt = 0


    def __new__(cls,*args,**kwargs):
        print("__new__")
        return super(Rectangle,cls).__new__(cls)


    def __call__(self) -> Any:
        print("__call__")

    def __init__(self,longueur=0,largeur=0) -> None:
        self._longueur = longueur
        self._largeur= largeur
        Rectangle._cpt+=1

    @classmethod
    def build_from_str(cls,value):
        value.split(',') # ['2','6']
        longueur,largeur =[int(i) for i in value.split(',')] 
        return cls(longueur,largeur)
    @property
    def longueur(self):
        return self._longueur
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,value):
        self._longueur = value
    @largeur.setter
    def largeur(self,value):
        self._largeur = value


    def get_surface(self):
        return self._longueur*self._largeur

    @staticmethod
    def get_cpt():
        return Rectangle._cpt

    def __str__(self) -> str:
        # return f"Rectangle longueur:{self._longueur}, largeur:{self._largeur}"
        return f"Rectangle {self._longueur=},{self._largeur=}"

    def __eq__(self, __value: object) -> bool:
        return self._longueur == __value._longueur and self._largeur == __value._largeur

    def __del__(self):
        print("Destructeur")
        Rectangle._cpt-=1