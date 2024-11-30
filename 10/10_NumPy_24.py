import numpy as np
def peak_indexes(arr):
    a = arr[:-2:1]
    b = arr[1:-1:1]
    c = arr[2::1]
    return np.arange(1, len(arr)-1, 1)[(b > a)&(b > c)]
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip())