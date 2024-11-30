import numpy as np

def mult_table(nrows, ncols):
    col = np.arange(1, ncols+1, 1)
    row = np.arange(1, nrows+1, 1).reshape((nrows, 1))
    return col*row

exec(input().strip())