xb = input().split()
yb = input().split()
list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
ok_x = 0; ok_y = 0
i = 0
while(not(ok_x) or not(ok_y)):
    if(not(ok_x) and xb[1] == list_of_months[i]):
        xb[1] = i
        ok_x = 1
    if(not(ok_y) and yb[1] == list_of_months[i]):
        yb[1] = i
        ok_y = 1
    i += 1
xb[2] = xb[2][:-1:1]
yb[2] = yb[2][:-1:1]
name_x = xb[0]
name_y = yb[0]
xb = [int(xb[3]), int(xb[2]), int(xb[1])]
yb = [int(yb[3]), int(yb[2]), int(yb[1])]
if(xb < yb):
    print(name_x)
elif(xb > yb):
    print(name_y)
else:
    print(name_x, name_y)
