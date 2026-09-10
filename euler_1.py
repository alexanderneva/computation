import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

def f(x,t):
#    return np.cos(x**2+t)
    ans = np.log(1 + t**2 + x**2)
    return ans

def euler(f,x,a,b,n):
    h = (b - a) / n
    t = a
    points = np.zeros([2,n])
    for k in range(n):
        x += np.exp(h*f(x,t))
        t += h
        points[0,k] = x 
        points[1,k] = t
    return points

points = euler(f,-4,0,2,50)

plt.plot(points[0],points[1])
plt.show()
