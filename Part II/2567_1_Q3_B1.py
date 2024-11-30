def display(gen, lists):
    print("%s : " %(gen), end = "")
    if(len(lists) == 0):
        print("Not found")
    else:
        for g in lists:
            print(g[1], end = " ")
    print()
    return

x = None
S = []
B = []
X = []
Y = []
Z = []
A = []
while(1):
    x = input()
    if(x == "-1"):
        break
    x = x.split()
    x[1] = [int(e) for e in x[1].split("/")]
    if(2468 <= x[1][2] <= 2488):
        S.append([[x[1][2], x[1][1], x[1][0]], x[0]])
    elif(2489 <= x[1][2] <= 2507):
        B.append([[x[1][2], x[1][1], x[1][0]], x[0]])
    elif(2508 <= x[1][2] <= 2523):
        X.append([[x[1][2], x[1][1], x[1][0]], x[0]])
    elif(2524 <= x[1][2] <= 2539):
        Y.append([[x[1][2], x[1][1], x[1][0]], x[0]])
    elif(2540 <= x[1][2] <= 2555):
        Z.append([[x[1][2], x[1][1], x[1][0]], x[0]])
    elif(x[1][2] > 2555):
        A.append([[x[1][2], x[1][1], x[1][0]], x[0]])
S.sort(reverse = True)
B.sort(reverse = True)
X.sort(reverse = True)
Y.sort(reverse = True)
Z.sort(reverse = True)
A.sort(reverse = True)
n = int(input())
for i in range(0, n, 1):
    gen = input()
    if(gen == 'S'):
        display(gen, S)
    elif(gen == 'B'):
        display(gen, B)
    elif(gen == 'X'):
        display(gen, X)
    elif(gen == 'Y'):
        display(gen, Y)
    elif(gen == 'Z'):
        display(gen, Z)
    elif(gen == 'A'):
        display(gen, A)