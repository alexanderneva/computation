import math
import matplotlib.pyplot as plt
import numpy as np

n = 30
h = 1
error_max = 0.
x = 0.5

for i in range(n):
    h = 0.5*h
    y = (math.sin(x+h)-math.sin(x))/h
    error = abs(math.cos(x)-y)
    if error > error_max:
        emax = error
        imax = i

#print(imax,emax)


def f(x,y):
    return x**2+y**2

def linear_j(f,x0,y0,step_size):
    h = step_size
    f_0 = f(x0,y0)
    delta_x = (f(x0+h,y0) - f_0 ) / h
    delta_y = (f(x0,y0+h) - f_0 ) / h
    delta = np.array([delta_x,delta_y])
    return delta


x = np.linspace(0,1,100)
X,Y=np.meshgrid(x,x)
print(linear_j(f,X,Y,1e-3))
