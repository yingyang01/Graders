a = float(input())
l = 0
r = 0
mid = 0
temp = a
while(temp):
    temp //= 10
    r += 1
while(1):
    mid = l+(r-l)/2
    if(abs(10**mid-a) <= 1e-10*max(a, 10**mid)):
        break
    elif(10**mid > a):
        r = mid
    else:
        l = mid
print(round(mid, 6))