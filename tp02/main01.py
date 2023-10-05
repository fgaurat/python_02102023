def make_incrementor(n):
    print('make_incrementor')
    def inc_function(inc):
        r = list(range(10000))
        print(len(r))
        print('inc_function')
        return inc+n

    return inc_function


def main():
    f = make_incrementor(42)
    r = f(0)
    print(r)
    r = f(1)
    print(r)


if __name__=='__main__':
    main()
