def read(file):
    strg = file.readline()
    if(len(strg) == 0):
        return "", ""
    a, b = strg.split()
    return a, b

s1, s2 = input().split()
f1 = open(s1, "r"); f2 = open(s2, "r")
id1, score1 = read(f1)
id2, score2 = read(f2)
while(len(id1) and len(id2)):
    if(id1[-2::1] == id2[-2::1]):
        if(id1 < id2):
            print(id1, score1)
            id1, score1 = read(f1)
        else:
            print(id2, score2)
            id2, score2 = read(f2)
    else:
        if(id1[-2::1] < id2[-2::1]):
            print(id1, score1)
            id1, score1 = read(f1)
        else:
            print(id2, score2)
            id2, score2 = read(f2)
while(len(id1)):
    print(id1, score1)
    id1, score1 = read(f1)
while(len(id2)):
    print(id2, score2)
    id2, score2 = read(f2)