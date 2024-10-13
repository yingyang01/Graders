def gcd(a, b):
    if(a > b):
        a, b = b, a
    while(a%b != 0):
        a, b = b, a%b
    return b

def is_coprime(a, b, c):
    ab = gcd(a, b)
    bc = gcd(b, c)
    ac = gcd(a, c)
    mn = min([ab, bc, ac])
    if(mn == 1):
        return True
    for i in range(2, mn+1):
        if(ab%i == 0 and bc%i == 0 and ac%i == 0):
            return False
    return True

def primitive_Pythagorean_triples(max_len):
    m = 2
    PPT = []
    while(1):
        n = 1
        if(m**2+n**2 > max_len):
            break
        while(m > n):
            if(gcd(m, n) != 1):
                n += 2
            a = 2*m*n
            b = m**2-n**2
            c = m**2+n**2
            mx = max([a, b, c])
            if(c > max_len):
                break
            # if(is_coprime(a, b, c)):
            PPT.append([min(a, b), max(a, b), c])
            n += 2
        m += 2
    m = 3
    while(1):
        n = 2
        if(m**2+n**2 > max_len):
            break
        while(m > n):
            if(gcd(m, n) != 1):
                n += 2
                continue
            a = 2*m*n
            b = m**2-n**2
            c = m**2+n**2
            if(c > max_len):
                break
            # if(is_coprime(a, b, c)):
            PPT.append([min(a, b), max(a, b), c])
            n += 2
        m += 2
    PPT.sort(key = lambda x : (max(x), x[0]))
    return PPT

exec(input())