def do_the_log(prefix=""):
    print("do_the_log")
    def wrapper_f(func):
        def wrapper(*args,**kwargs):
            print(f"{prefix} args",args,kwargs,func.__name__)
            r = func(*args,**kwargs)
            print(f"{prefix} return",r)
            return r
        return wrapper
    return wrapper_f


@do_the_log('LELOG')
# @do_the_log()
# @do_the_log
def say_hello(name):
    hello = f"Hello {name}"
    return hello


def main():
    r = say_hello("Fred")
    print(r)
    pass


if __name__=='__main__':
    main()
