def mult2(values):
    r = []
    for v in values:
        r.append(v*2)    
    return r 


# def mult2item(value):
#     return value*2

def main():
    l = [10,20,30]
    # r = mult2(l)
    # mult2item = lambda value:value*2

    r = list(map(lambda value:value*2,l))
    
    print(r) # [20,40,60]

    r = [value*2 for value in l]
    print(r)

    l=["   value01 ","   value02","value03     "]
    clean_l = [value.strip() for value in l]
    print(clean_l)


if __name__=='__main__':
    main()
