date, st, m, s = input().split()
st = float(st)
m = int(m)
s = int(s)
date = [int(e) for e in date.split("/")]
x = s
for i in range(1, m+1, 1):
    percent = 0
    if(i%4 == 1):
        percent = 1
    elif(i%4 == 2):
        percent = 2
    elif(i%4 == 3):
        percent = 3
    else:
        percent = 4
    if(x == date[1]):
        percent += 1
    st += st*percent/100/12
    x += 1
    if(x > 12):
        x = 1
print(round(st, 2))
