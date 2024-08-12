def make_int_list(x):
    return [int(e) for e in x.split()]

def is_odd(e):
    return e&1 == 1

def odd_list(alist):
    temp = []
    for e in alist:
        if(is_odd(e)):
            temp.append(e)
    return temp

def sum_square(alist):
    sgm = 0
    for e in alist:
        sgm += e*e
    return sgm

exec(input().strip())
    