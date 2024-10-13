d1 = {}
d2 = {}
file1 = open(input(), "r")
file2 = open(input(), "r")
file3 = open(input(), "r")
while(1):
    x = file1.readline().strip('\n')
    if(x == ''):
        break
    x = x.split(',')
    d1[x[0]] = x[1]
while(1):
    x = file2.readline().strip('\n')
    if(x == ''):
        break
    x = x.split(',')
    d2[x[0]] = x[1]
while(1):
    x = file3.readline().strip('\n')
    if(x == ''):
        break
    x = x.split(',')
    if(d1.get(x[0]) == None or d2.get(x[1]) == None):
        print("record error")
    else:
        print(d1[x[0]]+','+d2[x[1]])