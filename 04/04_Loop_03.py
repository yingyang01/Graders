a = input()
b = input()
if(len(a) != len(b)):
    print("Incomplete answer")
else:
    sz_a = len(a)
    cnt = 0
    for i in range(sz_a):
        if(a[i] == b[i]):
            cnt += 1
    print(cnt)