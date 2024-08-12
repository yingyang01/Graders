data = [float(e) for e in input().split()]
sz = len(data)
cnt = 0
if(sz == 1):
    print(1)
else:
    for i in range(sz):
        if(i and i != sz-1 and data[i] > data[i-1] and data[i] > data[i+1]):
            cnt += 1
    print(cnt)