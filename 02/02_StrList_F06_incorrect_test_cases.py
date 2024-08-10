def add_vector(u, v):
    ans = [0, 0, 0]
    print("{uu} + {vv} = ".format(uu = u, vv = v), end = "")
    for i in range(3):
        ans[i] = u[i]+v[i]
    return ans
    
A = input()
B = input()
a = ["", "", ""]
b = ["", "", ""]
sz_A = len(A)
sz_B = len(B)
i = 0
counters = 0
temp = ""
while(i < sz_A):
    ok = 0
    while(A[i] == '-' or (A[i] >= '0' and A[i] <= '9') or A[i] == '.'):
        temp += A[i]
        i += 1
        ok = 1
    if(ok):
        a[counters] = temp
        counters += 1
        temp = ""
        continue
    i += 1
counters = 0
i = 0
while(i < sz_B):
    ok = 0
    while(B[i] == '-' or (B[i] >= '0' and B[i] <= '9') or B[i] == '.'):
        temp += B[i]
        i += 1
        ok = 1
    if(ok):
        b[counters] = temp
        counters += 1
        temp = ""
        continue
    i += 1
for i in range(3):
    sz = len(a[i])
    ok = 0
    for j in range(sz):
        if(a[i][j] == '.'):
            ok = 1
            break
    if(ok == 0):
        a[i] = float(int(a[i]))
    else:
        a[i] = float(a[i])
    sz = len(b[i])
    ok = 0
    for j in range(sz):
        if(b[i][j] == '.'):
            ok = 1
            break
    if(ok == 0):
        b[i] = float(int(b[i]))
    else:
        b[i] = float(b[i])
print(add_vector(a, b))
