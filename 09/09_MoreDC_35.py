n = int(input())
lists = []
res = []
conditions = []
for i in range(n):
    lists.append(input().split())
conditions = input().split()
for i in range(n):
    ok = 0
    for j in range(0, len(conditions), 1):
        ok = 0
        for k in range(1, len(lists[i]), 1):
            if(conditions[j] == lists[i][k]):
                ok = 1
                break
        if(not(ok)):
            break
    if(ok):
        res.append(lists[i])
if(len(res)):
    res.sort()
    for i in range(len(res)):
        for j in range(len(res[i])):
            if(j != len(res[i])-1):
                print(res[i][j], end = ' ')
            else:
                print(res[i][j])
else:
    print("Not Found")