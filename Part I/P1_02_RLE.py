op = input()
if(op == "str2RLE"):
    strgs = input()
    prev = strgs[0]
    consec = 1
    RLE = []
    for i in range(1, len(strgs), 1):
        if(strgs[i] == prev):
            consec += 1
        else:
            RLE.append((prev, consec))
            consec = 1
            prev = strgs[i]
    RLE.append((prev, consec))
    for first, second in RLE:
        print("%s %d " %(first, second), end = '')
elif(op == "RLE2str"):
    RLE = input().split()
    strgs = ""
    for i in range(0, len(RLE), 2):
        for j in range(0, int(RLE[i+1]), 1):
            strgs += RLE[i]
    print("%s" %(strgs))
else:
    print("Error")
