n = int(input())
Union = set()
Intersect = set()
temp = set()
for i in range(0, n, 1):
    x = input().split()
    for e in set(x):
        Union.add(e)
        if(i == 0):
            Intersect = set(x)
            continue
        if(e in Intersect):
            temp.add(e)
    if(i):
        Intersect = temp
        temp = set()
print("{}\n{}".format(len(Union), len(Intersect)))

