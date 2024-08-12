def is_prime(n):
    if(n <= 1):
        return 0
    for k in range(2, int(n**0.5)+1):
        if(n%k == 0):
            return 0
    return 1

def next_prime(N):
    i = N+1
    while(not(is_prime(i))):
        i += 1
    return i

def next_twin_prime(N):
    cur = N+1
    while(1):
        if(is_prime(cur) and is_prime(cur+2)):
            return cur, cur+2
        cur += 1

exec(input().strip())