import copy


def main():
    a = "Python"
    print(hex(id(a)))
    print(a)
    # a[0] = 'J'
    a = "Java"
    print(hex(id(a)))

    a =1
    print(a)
    print(hex(id(a)))

    a =2
    b =2
    print(a,b)
    print(hex(id(a)))
    print(hex(id(b)))

    print("valeur a "*a)
    print(50*'-')
    the_l = [10,20,30,40,50]
    # the_l1=the_l.copy()
    the_l1=the_l[:]
    # the_l1=the_l[:]
    the_l1=copy.copy(the_l)
    the_l[0] = 1000
    print(the_l)
    print(the_l1)
    print(50*'-')
    the_l = [
        [10,20,30],
        [40,50,60],
        [70,90,90],
    ]

    # the_l1 = the_l[:] shallow copy ! 
    the_l1 = copy.deepcopy(the_l) 
    the_l[1][1] = 1000
    print(the_l)
    print(the_l1)
if __name__=='__main__':
    main()
