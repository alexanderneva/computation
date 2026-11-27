import numpy as np 
import matplotlib.pyplot as plt

def lorenz(t,u,v,w):
    u_t = -10*u + 10*v
    v_t = 28*u - v - u*w
    w_t = -8/3*w +u*v
    return u_t, v_t, w_t


def taylor_system_3(f,u,v,w,a=0,b=1,n=100):
    """Second Order Approximation for 3-dim Lorenz"""
    t = a
    h = (b - a) / n
    points = np.zeros([4,n])
    for k in range(n):
        points[0,k] = t
        points[1,k] = u
        points[2,k] = v
        points[3,k] = w

        u_p,v_p,w_p = f(t,u,v,w)
        u_pp = -10*u_p + 10*v_p
        v_pp = 28*u_p - v_p -(u*w_p+u_p*w)
        w_pp = -(8/3)*w_p + (u_p*v + u*v_p)

        u += h*(u_p + 0.5*h*(u_pp)) 
        v +=  h*(v_p + 0.5*h*(v_pp)) 
        w +=  h*(w_p + 0.5*h*(w_pp)) 
        t += h

    return points

def plot_lorenz(n_curves=3,max_time=3,max_step=100):
    """Plot the Lorenz system for random initial conditions"""
    loc = np.random.randint(-5,5)
    grid = np.random.normal(loc=loc,scale=1.5,size=(n_curves,3))
    ax = plt.figure().add_subplot(projection='3d')
    for ip in grid:
        print(ip)
        t,u,v,w = taylor_system_3(lorenz,ip[0],ip[1],ip[2],0,max_time,max_step)
        ax.plot(u,v,w, label =f'2nd order lorenz solution at ip {ip}')
    #ax.legend(loc='lower center')
    plt.title(f"Order 2 solutions for Lorenz Equation, random IC")
    plt.savefig('odes/lorenz.jpg',dpi=150)
    plt.show()

plot_lorenz(10,5)
