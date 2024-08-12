n = int(input())
lists = []; f = 1
for i in range(n):
    if(f == 1):
        lists.append(input())
        f = -1
    else:
        lists = [input()]+lists
        f = 1
for e in input().split():
    if(f == 1):
        lists.append(e)
        f = -1
    else:
        lists = [e]+lists
        f = 1
n = input()
while(n != "-1"):
    if(f == 1):
        lists.append(n)
        f = -1
    else:
        lists = [n]+lists
        f = 1
    n = input()
print([int(e) for e in lists])
