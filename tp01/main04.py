from collections import deque

def main():
    l = [10,20,30]

    l.append(40)

    print(l)
    
    last_value = l.pop()
    print(last_value)
    print(l)
    l.insert(0,0)
    print(l)

    de = deque(l)
    print(de)

if __name__=='__main__':
    main()
