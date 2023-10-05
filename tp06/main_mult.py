

class A:
    def __init__(self,value) -> None:
        self.value = value
    
    def the_method(self):
        print(f"the_method A {self.value=} {self.__class__.__name__=}")

class B(A):
    def __init__(self,value) -> None:
        self.value = value
    
    def the_method(self):
        print(f"the_method B {self.value=} {self.__class__.__name__=}")

class C(A):
    def __init__(self,value) -> None:
        self.value = value
    
    def the_method(self):
        print(f"the_method C {self.value=} {self.__class__.__name__=}")

class D(B,C):
    def __init__(self,value) -> None:
        self.value = value
    
    def the_method(self):
        super(C,self).the_method()
        print(f"the_method D {self.value=}")



def main():
    d = D(1)
    d.the_method()

    print(D.mro())

if __name__=='__main__':
    main()
