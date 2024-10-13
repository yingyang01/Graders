def factor(N):
    factors = []
    i = 2
    while(N != 1):
        consec = 0
        while(N%i == 0):
            N //= i
            consec += 1
        if(consec):
            factors.append([i, consec])
        i += 1
    return factors

exec(input().strip())
