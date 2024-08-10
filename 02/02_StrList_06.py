a = input().split(", ")
b = input().split(", ")
a[0] = (a[0])[1:]
b[0] = (b[0])[1:]
a[2] = (a[2])[:len(a[2])-1]
b[2] = (b[2])[:len(b[2])-1]
c = [0, 0, 0]
for i in range(3):
    a[i] = float(a[i])
    b[i] = float(b[i])
    c[i] = a[i]+b[i]
print(a, '+', b, '=', c)
