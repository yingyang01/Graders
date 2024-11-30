h = int(input())
picture = []
for i in range(0, h, 1):
    picture.append(list(input()))
op = input()
if(op == "rot90"):
    for j in range(0, len(picture[0]), 1):
        for i in range(h-1, -1, -1):
            print(picture[i][j], end = "")
        print()
else:
    for i in range(h-1, -1, -1):
        for j in range(len(picture[0])-1, -1, -1):
            print(picture[i][j], end = "")
        print()