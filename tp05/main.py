from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print(f"{c.cote=}")
    c.cote = 5
    print(f"{c.get_surface()=}")
    print(c)
    
    print(50*'-')
    
    ce = Cercle(2)
    # print(ce)
    # print(f"{ce.get_surface()=}")

if __name__=='__main__':
    main()
