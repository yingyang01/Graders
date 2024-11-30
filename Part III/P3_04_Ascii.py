import numpy as np

def display(arr):
    for i in range(0, arr.shape[0], 1):
        for j in range(0, arr.shape[1], 1):
            print(arr[i][j], end = "")
        print()
    return

def lstrip(arr):
    while(1):
        ok = 1
        for i in range(0, arr.shape[1]):
            if(arr[0][i] != '.'):
                ok = 0
                break
        if(not(ok)):
            break
        arr = arr[1::1]
    return arr

def rstrip(arr):
    while(1):
        ok = 1
        for i in range(0, arr.shape[1]):
            if(arr[arr.shape[0]-1][i] != '.'):
                ok = 0
                break
        if(not(ok)):
            break
        arr = arr[:arr.shape[0]-1:1]
    return arr

def strip_all(arr):
    arr = list(arr)
    cur = 0
    while(cur < len(arr)):
        ok = 1
        for j in range(0, len(arr[cur])):
            if(arr[cur][j] != '.'):
                ok = 0
        if(not(ok)):
            cur += 1
            continue
        arr.pop(cur)
    return np.array(arr)

file_name = input()
op = input()
file = open(file_name, "r")
ascii = []
while(1):
    x = file.readline().strip()
    if(len(x) == 0):
        break
    ascii.append(list(x))
ascii = np.array(ascii).T
if(op == "LSTRIP"):
    ascii = lstrip(ascii)
    display(ascii.T)
elif(op == "RSTRIP"):
    ascii = rstrip(ascii)
    display(ascii.T)
elif(op == "STRIP"):
    ascii = lstrip(ascii)
    ascii = rstrip(ascii)
    display(ascii.T)
elif(op == "STRIP_ALL"):
    ascii = strip_all(ascii)
    display(ascii.T)
else:
    print("Invalid command")
