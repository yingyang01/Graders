from math import sqrt
def sqrt_n_times(x, n):
    ans = x
    for i in range(n):
        ans = sqrt(ans)
    return ans

def cube_root(y):
    ans = sqrt_n_times(y, 2)
    i = 2
    while(i <= 32):
        ans *= sqrt_n_times(ans, i)
        i *= 2
    return ans

def main():
    q = float(input())
    print(cube_root(q))

exec(input())