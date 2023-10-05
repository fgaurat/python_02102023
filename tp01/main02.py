def pos_only(name,firstName,/):
    print("Hello",name,firstName)

def kw_only(*,name,firstName):
    print("Hello",name,firstName)

def add(*l):
    print(l)
    r=0

    for i in l:
        r+=i
    return r

def hello_world(**p):
    print(p)
    name = p['name']
    firstName = p['firstName']
    print("Hello",name,firstName)

def main():
    l = [10,20,30]
    a,*b=l
    print(a,b)
    # a,b,c,d=0,1
    print(type(a))

    r =add(*l)
    # r =add(10,20,30)
    
    r =add(10,20,30,40,50)
    print(r) # 60
    hello_world(name="GAURAT",firstName="Fred")
    
    d = {'name': 'GAURAT', 'firstName': 'Fred'}
    hello_world(**d)
    pos_only("GAURAT","Fred") # OK
    # pos_only(name="GAURAT",firstName="Fred") # KO
    kw_only(name="GAURAT",firstName="Fred") # KO




if __name__=='__main__':
    main()
