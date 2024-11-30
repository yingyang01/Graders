op = input().strip()
n = int(input().strip())
lists = []
x = input().strip()
lists.append(x)
prev = len(x)
error = 0
for i in range(1, n, 1):
    x = input().strip()
    if(len(x) != prev):
        error = 1
    lists.append(x)
if(error):
    print("Invalid size")
else:
    if(op == "90"):
        for i in range(0, prev, 1):
            for j in range(n-1, -1, -1):
                print(lists[j][i], end = '')
            print()
    elif(op == "flip"):
        for i in range(0, n, 1):
            for j in range(prev-1, -1, -1):
                print(lists[i][j], end = '')
            print()
    else:
        for i in range(n-1, -1, -1):
            for j in range(prev-1, -1, -1):
                print(lists[i][j], end = '')
            print()

