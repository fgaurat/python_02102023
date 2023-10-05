from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(5,2)
    r1 = Rectangle(5,2)

    print("longueur",r.longueur)
    l = r.longueur
    r.longueur=12 
    print("longueur",r.longueur)
    s = r.get_surface()
    print(s)#24
    
    rs = str(r)
    print(rs)


    # if r.__eq__(r1):
    if r == r1:
        print("ok")
    else:
        print("ko")

    print(50*'-')
    dr = DataRectangle(5,2)
    print(dr)
    print(dr.get_surface())

if __name__=='__main__':
    main()
