d, m, y = [int(e) for e in input().split()]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if(m == 2):
    if(d <= 13):
        d += 15
    else:
        if((y-543)%400 == 0 or ((y-543)%4 == 0 and (y-543)%100)):
            d = (d+15)%29
            if(d == 0):
                d = 29
            m += 1
            if(m > 12):
                m %= 12
                if(m == 0):
                    m = 12
                y += 1
        else:
            d = (d+15)%28
            m += 1
            if(m > 12):
                m %= 12
                if(m == 0):
                    m = 12
                y += 1
else:
    d += 15
    if(d > months[m-1]):
        d %= months[m-1]
        if(d == 0):
            d = months[m-1]
        m += 1
        if(m > 12):
            m %= 12
            if(m == 0):
                m = 12
            y += 1
print("{}/{}/{}".format(d, m, y))
