import numpy as np

def get_column_from_bottom_to_top(A, c):
    return A.T[c][::-1]

def get_odd_rows(A):
    return A[1::2]

def get_even_column_last_row(A):
    return A[-1][::2]

def get_diagonal1(A):
    k = np.identity(A.shape[0], int)*A
    return np.array([k[i][i] for i in range(0, A.shape[0])])

def get_diagonal2(A):
    k = np.identity(A.shape[0], int)[::-1]*A
    return np.array([k[i][A.shape[0]-i-1] for i in range(0, A.shape[0])])

exec(input().strip())