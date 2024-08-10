a = float(input())
l = 0
r = 3
mid = 0
while(1):
    mid = l+(r-l)/2
    if(abs(10**mid-a) <= (1e-10)*max(a, 10**mid)):
        break
    elif(10**mid > a):
        r = mid
    else:
        l = mid
print(round(mid, 6))