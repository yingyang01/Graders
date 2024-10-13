def add_poly(p1, p2):
    ptr1 = 0
    ptr2 = 0
    sz_p1 = len(p1)
    sz_p2 = len(p2)
    res = []
    while(ptr1 < sz_p1 and ptr2 < sz_p2):
        e1 = p1[ptr1]; e2 = p2[ptr2]
        if(e1[1] > e2[1]):
            res.append(e1)
            ptr1 += 1
        elif(e1[1] < e2[1]):
            res.append(e2)
            ptr2 += 1
        else:
            if(e1[0]+e2[0]):
                res.append((e1[0]+e2[0], e1[1]))
            ptr1 += 1
            ptr2 += 1
    while(ptr1 < sz_p1):
        res.append(p1[ptr1])
        ptr1 += 1
    while(ptr2 < sz_p2):
        res.append(p2[ptr2])
        ptr2 += 1
    return res

def mult_poly(p1, p2):
    temp = []
    res = []
    for i in range(0, len(p1), 1):
        for j in range(0, len(p2), 1):
            temp.append((p1[i][0]*p2[j][0], p1[i][1]+p2[j][1]))
    temp.sort(key = (lambda x : -x[1]))
    i = 0; prev = 1e10; coeff = 0
    sz_temp = len(temp)
    while(i < sz_temp):
        if(temp[i][1] != prev):
            if(coeff):
                res.append((coeff, prev))
            prev = temp[i][1]
            coeff = 0
        coeff += temp[i][0]
        i += 1
    if(coeff):
        res.append((coeff, prev))
    return res

for i in range(3):
    exec(input().strip())