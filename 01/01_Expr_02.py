from math import sqrt
a = [0, 0, 0]
for i in range(3):
    a[i] = float(input())
print(round((-a[1]-sqrt(a[1]*a[1]-4*a[0]*a[2]))/(2*a[0]), 3), round((-a[1]+sqrt(a[1]*a[1]-4*a[0]*a[2]))/(2*a[0]), 3))
