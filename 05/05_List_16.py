n = int(input())
collatz = []
while(n != 1):
    collatz.append(n)
    if(n&1):
        n = 3*n+1
    else:
        n //= 2
collatz.append(1)
collatz = collatz[-15::]
for e in collatz:
    if(e != 1):
        print("{}->".format(e), end = '')
    else:
        print(e)
