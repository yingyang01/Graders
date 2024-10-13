def pattern1(nrows, ncols):
    pattern = []
    sub_pattern = []
    cnt = 1
    for i in range(0, nrows, 1):
        for j in range(0, ncols, 1):
            sub_pattern.append(cnt)
            cnt += 1
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

def pattern2(nrows, ncols):
    pattern = []
    sub_pattern = []
    for i in range(0, nrows, 1):
        cur = i+1
        for j in range(0, ncols, 1):
            sub_pattern.append(cur)
            cur += nrows
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

def pattern3(N):
    pattern = []
    sub_pattern = []
    cnt = 1
    for i in range(0, N, 1):
        for j in range(0, i, 1):
            sub_pattern.append(0)
        for j in range(i, N, 1):
            sub_pattern.append(cnt)
            cnt += 1
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

def pattern4(N):
    pattern = []
    sub_pattern = []
    st = 1
    for i in range(0, N, 1):
        for j in range(0, i, 1):
            sub_pattern.append(0)
        st += i
        cur = st
        for j in range(i, N, 1):
            sub_pattern.append(cur)
            cur += j+2
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

def pattern5(N):
    pattern = []
    sub_pattern = []
    for i in range(0, N, 1):
        for j in range(0, i, 1):
            sub_pattern.append(0)
        cur = i+1
        diff = N
        for j in range(i, N, 1):
            sub_pattern.append(cur)
            cur += diff
            diff -= 1
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

def pattern6(N):
    pattern = []
    sub_pattern = []
    sgm = N*(N+1)//2
    for i in range(0, N, 1):
        for j in range(0, i, 1):
            sub_pattern.append(0)
        cur = i+1
        state = 0
        for j in range(i, N, 1):
            sub_pattern.append(cur)
            if(not(state)):
                state = 1
                if(i == 0 and j == N-2 and N%2 == 0):
                    cur = sgm
                else:
                    cur += 2*(N-1-j)
            else:
                state = 0
                cur += 2*(i+1)-1
        pattern.append(sub_pattern)
        sub_pattern = []
    return pattern

exec(input().strip())