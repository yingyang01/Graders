mx = ""
mn = ""
choice = input()
f = 1
while(choice != "Zig-Zag" and choice != "Zag-Zig"):
    x, y = choice.split()
    if(f == 1):
        mn += x+','
        mx += y+','
        f = -1
    elif(f == -1):
        mn += y+','
        mx += x+','
        f = 1
    choice = input()
if(choice == "Zag-Zig"):
    mn, mx = mx, mn
mnn = 1e10
mxx = -1e10
for e in mn.split(','):
    if(e == ''):
        break
    mnn = min(mnn, int(e))
for e in mx.split(','):
    if(e == ''):
        break
    mxx = max(mxx, int(e))
print(mnn, mxx)