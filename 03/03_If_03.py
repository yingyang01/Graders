sc = list(map(float, input().split()))
sgm = 0
mx = -1
mn = 1e8
for i in range(4):
    sgm += sc[i]
    if(sc[i] > mx):
        mx = sc[i]
    if(sc[i] < mn):
        mn = sc[i]
print(round((sgm-mx-mn)/2, 2))