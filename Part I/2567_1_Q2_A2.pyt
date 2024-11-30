from math import floor
c, n = input().split()
c = float(c)
n = int(n)
lists = []
for i in range(0, n, 1):
    lists.append(floor(c))
    c -= floor(c)
    if(c < 1e-10):
        break
    c = 1/c
print(str(lists)[1:-1])