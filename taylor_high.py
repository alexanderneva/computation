import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return 1 + x**2 + t**2

print(f(1,1))

def taylor(f,x,a,b,n):
    h = (b-a)/n
    t = a
    points = np.zeros([2,n])
    for i in range(n):
        x_p = f(x,t)
        x_pp = 2*x*x_p + 3*t**2
        x_ppp = 2*x*x_pp + 2*x_p**2 + 6*t
        x_pppp = 2*x*x_p + 6*x_p*x_pp + 6
        x = h*(x_p + 0.5*h*(x_pp + (1/3)*h*(x_ppp + 0.25*h*x_pppp)))
        t = a + i*h
        points[0,i] = x
        points[1,i] = t
    return points


points = taylor(f,-4,1,2,100)
plt.plot(points[1],points[0])
plt.show()
