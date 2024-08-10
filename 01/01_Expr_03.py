def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n*factorial(n-1)
import math
a = round((math.pi-factorial(10)/(8**8)+math.log(9.7)**(7/(71**(1/2))-math.sin(40*math.pi/180)))/(1.2**2.3**(1/3)), 6)
print(a)
