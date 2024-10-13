def row_number(t, e):
    for i in range(0, len(t), 1):
        if(e in t[i]):
            return i
    return    

def flatten(t):
    flat = []
    for lists in t:
        for d in lists:
            if(d):
                flat.append(d)
    return flat

def inversions(x):
    cnt = 0
    for i in range(0, len(x)-1, 1):
        for j in range(i+1, len(x), 1):
            if(x[i] > x[j]):
                cnt += 1
    return cnt

def solvable(t):
    sz_rows = len(t)
    r = row_number(t, 0)
    t = flatten(t)
    cnt_inversions = inversions(t)
    if(sz_rows%2 and cnt_inversions%2 == 0):
        return True
    elif(sz_rows%2 == 0 and ((cnt_inversions%2 == 1 and r%2 == 0) or (cnt_inversions%2 == 0 and r%2 == 1))):
        return True
    return False

exec(input())