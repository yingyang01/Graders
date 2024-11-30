def spiral_square(n):
    hv = n//2
    pattern = []
    for i in range(0, n, 1):
        sub_pattern = []
        for j in range(0, n, 1):
            det = min([i, j, n-1-i, n-1-j])
            xrb = n-1-det
            yrb = n-1-det
            temp = (n-det*2)**2
            if(i == xrb):
                sub_pattern.append(temp-abs(yrb-j))
            elif(j == yrb):
                sub_pattern.append((n-(det+1)*2)**2+abs(xrb-i))
            elif(i == det):
                sub_pattern.append(temp-2*(n-1-det*2)-(j-det))
            else:
                sub_pattern.append(temp-(n-1-det*2)-(yrb-i))
        pattern.append(sub_pattern)
    return pattern
def print_square(S):
    for sub_pattern in S:
        print(" ".join([(" "*2+str(e))[-3::1] for e in sub_pattern]))
exec(input().strip())
