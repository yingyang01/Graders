D = [int(e) for e in input().split()]
P = sorted(D)
qs = 0
X = []
for i in range(0, len(P), 1):
    qs += P[i]
    X.append(D[qs%len(D)])
    D.pop(qs%len(D))
for d in X:
    print(d, end = " ")