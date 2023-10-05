


class Rectangle:

    def __init__(self,longueur=0,largeur=0) -> None:
        print("init Rectangle")
        self._longueur = longueur
        self._largeur= largeur

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

    def __str__(self) -> str:
        # return f"Rectangle longueur:{self._longueur}, largeur:{self._largeur}"
        return f"Rectangle {self._longueur=},{self._largeur=}"

    def __eq__(self, __value: object) -> bool:
        return self._longueur == __value._longueur and self._largeur == __value._largeur

    def __del__(self):
        print("Destructeur")