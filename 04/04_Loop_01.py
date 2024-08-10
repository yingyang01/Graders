sgm = 0
x = input()
ok = 0
while(x != 'q'):
    sgm += float(x)
    ok += 1
    x = input()
if(ok == 0):
    print("No Data")
else:
    print("{}".format(round(sgm/ok, 2)))
