mn = []
mx = []
n = int(input())
f = 1
for i in range(n):
    x, y = map(int, input().split())
    if(f == 1):
        mn.append(x)
        mx.append(y)
        f = -1
    else:
        mn.append(y)
        mx.append(x)
        f = 1
choice = input()
if(choice == "Zag-Zig"):
    mn, mx = mx, mn
mnn = 1e10
mxx = -1e10
for i in range(n):
    mnn = min(mnn, mn[i])
    mxx = max(mxx, mx[i])
print(mnn, mxx)

        
