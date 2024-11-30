def display(lists, k):
    for i in range(0, len(lists)//k, 1):
        for j in range(0, k, 1):
            if(j != k-1):
                print(lists[i*k+j], end = ",")
            else:
                print(lists[i*k+j])
    for j in range(0, len(lists)%k, 1):
        if(j != len(lists)%k-1):
            print(lists[len(lists)//k*k+j], end = ",")
        else:
            print(lists[len(lists)//k*k+j])
    return
n = int(input())
k = int(input())
if(n < 0 and k < 1):
    print("Invalid n and k")
elif(n < 0):
    print("Invalid n")
elif(k < 1):
    print("Invalid k")
else:
    top = ""
    dash = "-"*n
    for i in range(1, k+1, 1):
        if(i != k):
            top += (str(i)+dash)[0:n+1:1]
        else:
            top += (str(i)+dash)[0:n:1]
    gray = ["0", "1"]
    for i in range(1, n, 1):
        gray = gray+gray[-1::-1]
        gray = ['0'+c for c in gray[0:len(gray)//2:1]]+['1'+c for c in gray[len(gray)//2::1]]
    print(top)
    display(gray, k)