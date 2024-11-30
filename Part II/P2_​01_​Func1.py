def is_odd(n):
    return (n&1) == 1

def has_odds(x):
    for c in x:
        if(is_odd(c)):
            return True
    return False

def all_odds(x):
    for c in x:
        if(not(is_odd(c))):
            return False
    return True

def no_odds(x):
    if(has_odds(x)):
        return False
    else:
        return True
    
def get_odds(x):
    lists = []
    for e in x:
        if(is_odd(e)):
            lists.append(e)
    return lists

def zip_odds(a, b):
    a = get_odds(a); b = get_odds(b)
    zipped = []
    ptra, ptrb = 0, 0
    while(ptra < len(a) and ptrb < len(b)):
        zipped.append(a[ptra])
        zipped.append(b[ptrb])
        ptra += 1
        ptrb += 1
    while(ptra < len(a)):
        zipped.append(a[ptra])
        ptra += 1
    while(ptrb < len(b)):
        zipped.append(b[ptrb])
        ptrb += 1
    return zipped

exec(input().strip())

