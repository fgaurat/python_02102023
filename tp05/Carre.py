from Rectangle import Rectangle


class Carre(Rectangle):



    def __init__(self, cote=0) -> None:
        super().__init__(cote, cote)
        print("init Carre")
        self._cote = cote

    @property
    def cote(self):
        return self._cote
    
    @cote.setter
    def cote(self,value):
        self._cote = value
        self._longueur = value
        self._largeur = value

    def __str__(self) -> str:
        return f"{__class__.__name__} {self._cote=}"