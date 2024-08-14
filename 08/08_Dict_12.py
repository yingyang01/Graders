n = int(input())
names = {}
for i in range(0, n, 1):
    x = input().split()
    names[x[0]] = x[1]
    names[x[1]] = x[0]
m = int(input())
for i in range(0, m, 1):
    name = input()
    value = names.get(name)
    if(value == None):
        print("Not found")
    else:
        print(value)