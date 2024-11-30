import numpy as np

def get_column_from_bottom_to_top(A, c):
    arr = np.ndarray((A.shape[1], ), type(A[0][0]))
    for i in range(A.shape[1]-1, -1, -1):
        arr[A.shape[1]-i-1] = A[i][c]
    return arr

def get_odd_rows(A):
    arr = np.ndarray((A.shape[0]//2, A.shape[1]), type(A[0][0]))
    for i in range(0, A.shape[0]//2):
        for j in range(0, A.shape[1], 1):
            arr[i][j] = A[2*i+1][j]
    return arr

def get_even_column_last_row(A):
    arr = np.ndarray(((A.shape[1]+1)//2, ), type(A[0][0]))
    for i in range(0, A.shape[1], 2):
        arr[i//2] = A[A.shape[0]-1][i]
    return arr

def get_diagonal1(A):
    arr = np.ndarray((A.shape[1], ), type(A[0][0]))
    for i in range(0, A.shape[1], 1):
        arr[i] = A[i][i]
    return arr

def get_diagonal2(A):
    arr = np.ndarray((A.shape[1], ), type(A[0][0]))
    for i in range(0, A.shape[1], 1):
        arr[i] = A[i][A.shape[1]-i-1]
    return arr

exec(input().strip())