import numpy as np

def eq(A, B, p):
    dim = 1
    for i in A.shape:
        dim *= i
    return np.sum(A-B == 0) >= dim*p/100

def closest_point_indexes(points, p):
    dist = np.sqrt(np.sum((points-p)**2, axis=1))
    mn = np.min(dist)
    x = np.array([i for i in range(0, dist.shape[0]) if(dist[i] == mn)])
    return ""

def number_of_inversions(A):
    sgm = 0
    for i in range(0, A.shape[0]-1):
        sgm += np.sum(A[i+1::1] < A[i])
    return sgm

exec(input().strip())