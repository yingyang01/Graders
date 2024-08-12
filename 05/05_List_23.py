def cmp(e):
    return (e[0]**2+e[1]**2)**0.5
n = int(input())
dist = []
for i in range(n):
    pair = [float(e) for e in input().split()]+[i]
    dist.append(pair)
dist.sort(key = cmp)
print("#{}: ({}, {})".format(dist[2][2]+1, dist[2][0], dist[2][1]))