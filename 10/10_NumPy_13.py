import numpy as np

def p(X):
    return 1-(np.e**(np.sum(X*np.array([0.1, 0.5]), axis = 1)-3.98)+1)**-1

exec(input().strip())