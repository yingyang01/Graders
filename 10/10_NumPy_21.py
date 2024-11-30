import numpy as np

def sum_2_rows(M):
    r1 = M[::2]
    r2 = M[1::2]
    return r1+r2

def sum_left_right(M):
    c1 = M.T[:len(M)//2:1]
    c2 = M.T[len(M)//2::1]
    return (c1+c2).T

def sum_upper_lower(M):
    r1 = M[:len(M)//2:1]
    r2 = M[len(M)//2::1]
    return r1+r2

def sum_4_quadrants(M):
    Q1 = M[:len(M)//2:1, len(M)//2::1]
    Q2 = M[:len(M)//2:1, :len(M)//2:1]
    Q3 = M[len(M)//2::1, :len(M)//2:1]
    Q4 = M[len(M)//2::1, len(M)//2::1]
    return Q1+Q2+Q3+Q4

def sum_4_cells(M):
    return M[::2, ::2]+M[::2, 1::2]+M[1::2, ::2]+M[1::2, 1::2]

def count_leap_years(years):
    years -= 543
    return len(years[(years%400 == 0) | ((years%4 == 0) & (years%100 != 0))])

exec(input().strip())