n = int(input())
tree = {}
for i in range(0, n, 1):
    x = input().split(',')
    tree[x[0]] = [x[1], int(x[2])]
final = {}
for t in tree:
    sgm = 0
    while(t in tree):
        sgm += tree[t][1]
        tree[t][1] = 0
        t = tree[t][0]
    if(t not in final):
        final[t] = sgm
    else:
        final[t] += sgm
name = sorted([[-value, key] for [key, value] in final.items()])
for n in name:
    print("Boss "+n[1]+' '+str(-n[0]))