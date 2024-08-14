n = int(input())
maps = {}
for i in range(0, n, 1):
    x = input().split()
    if(len(x) == 3):
        x = [x[0]+' '+x[1], x[2]]
    maps[x[0]] = x[1]
    maps[x[1]] = x[0]
m = int(input())
for i in range(0, m, 1):
    x = input()
    print(x, "-->", end = ' ')
    value = maps.get(x)
    if(value == None):
        print("Not found")
    else:
        print(value)