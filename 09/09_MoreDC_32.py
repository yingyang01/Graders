def check_size(D):
    sz = 0
    for i in range(0, len(D), 1):
        sz += len(D[i])
    return sz

def first_fit(L, e):
    ok = 0
    for i in range(0, len(L), 1):
        sgm = 0
        for j in range(0, len(L[i]), 1):
            sgm += L[i][j]
        if(sgm+e <= 100):
            ok = 1
            L[i].append(e)
            break
    if(not(ok)):
        L.append([e])
    return

def best_fit(L, e):
    mn = 1e10
    pos = -1
    ok = 0
    for i in range(0, len(L), 1):
        sgm = 0
        for j in range(0, len(L[i]), 1):
            sgm += L[i][j]
        if(sgm+e <= 100 and 100-sgm-e < mn):
            mn = 100-sgm-e
            pos = i
    if(pos != -1):
        L[pos].append(e)
    else:
        L.append([e])
    return

def partition_FF(D):
    ans = []
    for i in range(0, len(D), 1):
        first_fit(ans, D[i])
    return ans

def partition_BF(D):
    ans = []
    for i in range(0, len(D), 1):
        best_fit(ans, D[i])
    return ans

exec(input().strip())