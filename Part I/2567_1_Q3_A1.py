a, b, c, d = [int(e) for e in input().split()]
if(a > 1):
    while(b < d):
        b += 1
        if(b <= c):
            break
        c += 3
else:
    a = b+c+d
    if(b > 7):
        if(b > 9):
            c = 2*d+2
            if(b > 12):
                c = 4*d
            if(b > 15):
                d = c-a
            else:
                d = c+2*a
            print(c, d)
        else:
            c = 3*d
    else:
        if(b > 5):
            b = c+d
        elif(b > 2):
            b = 2*c
        else:
            b = c-d
        print(a, b)
print(a, b, c, d)