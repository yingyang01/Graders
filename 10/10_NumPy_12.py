import numpy as np

def toCelsius(f):
    return 5/9*(f-32)

def BMI(wh):
    w = wh[::, 0::2].reshape(len(wh))
    h = wh[::, 1::2].reshape(len(wh))*0.01
    return w/h**2

def distanceTo(p, Points):
    return np.sqrt(np.sum((Points-p)**2, axis = 1))

exec(input().strip())