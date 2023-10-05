from Rectangle import Rectangle

def main():
    r = Rectangle(5,2)
    print(Rectangle.get_cpt())
    r1 = Rectangle(15,72)
    print(Rectangle.get_cpt())
    print(Rectangle.get_cpt())
    r2 = Rectangle(95,52)
    print(Rectangle.get_cpt())
    print(Rectangle.get_cpt())
    print(Rectangle.get_cpt())

    r3 = Rectangle.build_from_str('2,6')
    r3()

if __name__=='__main__':
    main()
