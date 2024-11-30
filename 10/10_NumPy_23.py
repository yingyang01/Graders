import numpy as np

def read_data():
    weight = np.array([float(e) for e in input().split()])
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    score = np.sum(data[::1, 1::1]*weight, axis = 1)
    average = np.sum(score)/len(data)
    data = data[score < average]
    if(len(data)):
        print(", ".join([str(data[i][0]) for i in range(0, len(data), 1)]))
    else:
        print("None")

exec(input().strip())