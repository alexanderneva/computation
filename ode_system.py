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

#print(taylor_system_2(f,2,-1,0,1,100))



t,x,y = taylor_system(f,1,0.2,1,3,200)
#print(t)
#print(x)

ax = plt.figure().add_subplot(projection='3d')
ax.scatter(t,x,y,zdir='t')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y')
plt.show()
plt.savefig("odes/taylor_system.jpg")


s0=0.999
gamma = 0.1
lamb = 0.59
r0 = s0*lamb / gamma

def sir(t,x,y,z):
    return -lamb*x*y, lamb*x*y - gamma*y,gamma*y



def taylor_system_3(f,s,i,r,a,b,n):
    """Second Order Approximation for 3-dim ode"""
    t = a
    h = (b - a) / n
    points = np.zeros([4,n])
    for k in range(n):
        s_p,i_p,r_p = f(t,s,i,r)
        s_pp = -lamb*(i_p*s + s_p*i)
        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
        r_pp = gamma*i_p

   #     x_ppp = x_pp - y_pp - 2 - 6*t
   #     y_ppp = x_pp + y_pp -8 + 6*t
   #     x_pppp = x_ppp - y_ppp - 6
   #     y_pppp = x_ppp + y_ppp + 6

        s += h*(s_p + 0.5*h*(s_pp)) 
        i +=  h*(i_p + 0.5*h*(i_pp)) 
        r +=  h*(r_p + 0.5*h*(r_pp)) 
        t += h
        points[0,k] = t
        points[1,k] = s
        points[2,k] = i
        points[3,k] = r

    return points

t,s,i,r = taylor_system_3(sir,s0,0.001,0,0,100,200)

plt.plot(t,s, label='susceptible')
plt.plot(t,i, label='infected')
plt.plot(t,r, label='recovered')
plt.xlabel('Time')
plt.ylabel('Percentage')
plt.title(f"Second order approx lambda {lamb} gamma {gamma}")
plt.legend()
plt.savefig('odes/sir_system_2.jpg')
plt.show()


def taylor_system_4(f,s,i,r,a,b,n):
    """Third Order Approximation for 3-dim ode"""
    t = a
    h = (b - a) / n
    points = np.zeros([4,n])
    for k in range(n):
        s_p,i_p,r_p = f(t,s,i,r)
        s_pp = -lamb*(i_p*s + s_p*i)
        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
        r_pp = gamma*i_p
        s_ppp = -lamb*(i_pp*s + 2*s_p*i_p + i*s_pp)
        i_ppp = s_ppp - gamma*i_pp
        r_ppp = gamma*i_pp


        s += h*(s_p + 0.5*h*(s_pp + h*(1/3)*s_ppp))
        i +=  h*(i_p + 0.5*h*(i_pp + h*(1/3)*(i_ppp))) 
        r +=  h*(r_p + 0.5*h*(r_pp + h*(1/3)*(r_ppp)))
        t += h
        points[0,k] = t
        points[1,k] = s
        points[2,k] = i
        points[3,k] = r

    return points


t,s,i,r = taylor_system_4(sir,s0,0.001,0,0,100,200)

plt.plot(t,s, label='susceptible')
plt.plot(t,i, label='infected')
plt.plot(t,r, label='recovered')
plt.xlabel('Time')
plt.ylabel('Percentage')
plt.title(f"Third order approx lambda {lamb} gamma {gamma}")
plt.legend()
plt.savefig('odes/sir_system_3.jpg')
plt.show()


def taylor_system_5(f,s,i,r,a,b,n):
    """Fourth Order Approximation for 3-dim ode"""
    t = a
    h = (b - a) / n
    points = np.zeros([4,n])
    for k in range(n):
        s_p,i_p,r_p = f(t,s,i,r)
        s_pp = -lamb*(i_p*s + s_p*i)
        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
        r_pp = gamma*i_p
        s_ppp = -lamb*(i_pp*s + 2*s_p*i_p + i*s_pp)
        i_ppp = s_ppp - gamma*i_pp
        r_ppp = gamma*i_pp
        s_pppp = -lamb*(i_ppp*s + 3*s_p*i_pp + 3*i_p*s_pp)
        i_pppp = s_pppp - gamma*i_ppp
        r_pppp = gamma*i_ppp

   #     x_ppp = x_pp - y_pp - 2 - 6*t
   #     y_ppp = x_pp + y_pp -8 + 6*t
   #     x_pppp = x_ppp - y_ppp - 6
   #     y_pppp = x_ppp + y_ppp + 6

        s += h*(s_p + 0.5*h*(s_pp + h*(1/3)*(s_ppp + h*0.25*s_pppp)))
        i +=  h*(i_p + 0.5*h*(i_pp + h*(1/3)*(i_ppp+ h*0.25*i_pppp))) 
        r +=  h*(r_p + 0.5*h*(r_pp + h*(1/3)*(r_ppp+ h*0.25*r_pppp)))
        t += h
        points[0,k] = t
        points[1,k] = s
        points[2,k] = i
        points[3,k] = r

    return points


t,s,i,r = taylor_system_5(sir,s0,0.001,0,0,100,200)

plt.plot(t,s, label='susceptible')
plt.plot(t,i, label='infected')
plt.plot(t,r, label='recovered')
plt.xlabel('Time')
plt.ylabel('Percentage')
plt.title(f"Fourth order approx lambda {lamb} gamma {gamma}")
plt.legend()
plt.savefig('odes/sir_system_4.jpg')
plt.show()
