import numpy as np
import matplotlib.pyplot as plt

def f(t,x,y):
    return x - y + t*(2-t*(1+t)), x + y + t**2 * (-4+t)



def taylor_system(f,x,y,a,b,n):
    t = a
    h = (b - a) / n
    points = np.zeros([3,n])
    for i in range(n):
        x_p,y_p = f(t,x,y)
        x_pp = x_p - y_p + 2 -t*(2+3*t)
        y_pp = x_p + y_p + t*(-8+3*t)
        x_ppp = x_pp - y_pp - 2 - 6*t
        y_ppp = x_pp + y_pp -8 + 6*t
        x_pppp = x_ppp - y_ppp - 6
        y_pppp = x_ppp + y_ppp + 6
        x = x + h*(x_p + 0.5*h*(x_pp + (1/3)*h*(x_ppp + 0.25 * h * x_pppp)))
        y = y + h*(y_p + 0.5*h*(y_pp + (1/3)*h*(y_ppp + 0.25 * h * y_pppp)))
        t = t + h
        points[0,i] = t
        points[1,i] = x
        points[2,i] = y

    return points


def taylor_system_2(f,x,y,a,b,n):
    t = a
    h = (b - a) / n
    points = np.zeros([2,4])
    xs = np.array([x,y])
    pos = xs 
    for i in range(n):
        points[0,0] = x - y + t*(2-t*(1+t))
        points[1,0] = x + y + t**2*(t-4)
        points[0,1] = points[0,0] + points[1,0] + 2 - t*(2+3*t)
        points[1,1] = points[0,0] + points[1,0] + t*(-8+3*t)
        points[0,2] = points[0,1] - points[1,1] - 2 - 6*t
        points[1,2] = points[0,1] + points[1,1] - 8 + 6*t
        points[0,3] = points[0,2] - points[1,2] - 6
        points[1,3] = points[0,2] + points[1,2] + 6
        for j in range(2):
            xs[j] = x + h*(points[j,0] + 0.5*h*(points[j,1] + (1/3)*h*(points[j,2]+0.25*h*points[j,3])))
        t += h
        print(f"{i,t,xs}")

    return xs

print(taylor_system_2(f,2,-1,0,1,100))



#t,x,y = taylor_system(f,1,0.2,1,3,200)
##print(t)
##print(x)
#
#ax = plt.figure().add_subplot(projection='3d')
#ax.scatter(t,x,y,zdir='t')
#ax.set_xlabel('t')
#ax.set_ylabel('x')
#ax.set_zlabel('y')
#plt.show()
