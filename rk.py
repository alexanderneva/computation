import numpy as np 
import matplotlib.pyplot as plt


def f(t,x):
    return 2 + (x-t-1)**2

def rk4(f,x,a,b,n):
    t = a 
    h = (b - a) / n 
    points = np.zeros([2,n])
    for i in range(n):
        points[0,i] = t
        points[1,i] = x
        k1 = h*f(t,x)
        k2 = h*f(t+0.5*h, x + 0.5*k1)
        k3 = h*f(t + 0.5*h, x + 0.5*k2)
        k4 = h*f(t+h, x + k3)
        x = x+ (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + i*h
    return points

def rk45(f,x,t,h,epsilon):
    c20, c21 = 0.25,0.25
    c30, c31, c32 = 0.375, 0.09375, 0.28125
    c40, c41 = 12./13., 1932./2197
    c42, c43 = -7200. / 2197, 7296./2197.
    c51, c52 = 439./216., -8.
    c53, c54 = 3680./513., -845./4104.
    c60, c61, c62 = 0.5, -8./27., 2.
    c63, c64 = -3544./2565., 1859. / 4104.
    c65 = -0.275
    a1,a2,a3 = 25. / 216., 0, 1408. / 2565.
    a4, a5 = 2197. / 4104., -0.2
    b1, b2, b3 = 16. / 135., 0., 6656. / 12825.
    b4, b5 = 28561. / 56430., -0.18
    b6 = 2. / 55.
    k1 = h*f(t,x)
    k2 = h*f(t+c20*h,x+c21*k1)
    k3 = h*f(t+c30*h, x + c31*k1 + c32*k2)
    k4 = h*f(t+c40*h, x + c41*k1 + c42*k2 + c43*k3)
    k5 = h*f(t+h, x + c51*k1 + c52*k2 + c53*k3 + c54*k4)
    k6 = h*f(t+c60*h, x + c61*k1 + c62*k2 + c64*k3 + c64*k4 + c65*k5)
    x4 = x + a1*k1 + a3*k3 + a4*k4 + a5*k5
    x = x + b1*k1 + b3*k3 + b4*k4 + b5*k5 + b6*k6
    t = t + h
    epsilon = np.abs(x-x4)
#    print(f"The {x} and {x4} with error {epsilon}")
    return t,x,epsilon

#t,x = rk4(f,2,1,2,50)
#print(f" {t} and {x}")
#plt.plot(t,x)
#plt.xlabel("time")
#plt.show()

def runrk(f,x,a,b,n):
    h = (b-a)/n
    t = a
    epsilon = 0
    points = np.zeros([3,n])
    for i in range(n):
        t,x,epsilon = rk45(f,x,t,h,epsilon)
        points[0,i] = t 
        points[1,i] = x 
        points[2,i] = epsilon
    return points

def rk45_adaptive(f,t=0.,x=0.,h=0.,tb=0.,itmax=0.,emax=0.,emin=0.,hmin=0.,hmax=0.,iflag=0.):
    delta = 0.5e-5
    iflag = 1
    k = 0
    epsilon = np.mean([emax,emin])
    times = []
    xs = []
    errors = []
    while k <= itmax: 
        k += 1
        if np.abs(h) < hmin:
            h = np.sign(h)*hmin
        elif np.abs(h) > hmax:
            h = np.sign(h)*hmax
        d = np.abs(tb-t)
        if d <= np.abs(h):
            iflag = 0
            if d <= delta*np.max(np.abs(tb),np.abs(t)):
                break
            h = np.sign(h)*d
        xsave = x
        tsave = t
        t,x,epsilon = rk45(f,x,t,h,epsilon)
        if iflag == 0:
            break
        if epsilon < emin:
            h = 2*h
        elif epsilon > emax:
            h = h/2
            x = xsave
            t = tsave
            k -= 1
        times.append(t)
        xs.append(x)
        errors.append(epsilon)
    times = np.array(times)
    xs = np.array(xs)
    errors = np.array(errors)

    return t,x,epsilon,(times,xs,errors)

itmax = 1000
iflag = 0
emax = 1e-5
emin = 1e-8
hmin = 1e-6
hmax = 1
t = 0
x = 0
h = 0.01
tb = 10
def f1(t,x):
    return 3 + 5*np.sin(t) + 0.2*x
t,x,epsilon,(times,xs,errors) = rk45_adaptive(f1,t,x,h,tb,itmax,emax,emin,hmin,hmax,iflag)

print(epsilon,errors.size,times.size)

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(times,xs)
ax1.set_title("x")
ax2.plot(times,errors)
ax2.set_title("error")
plt.show()


#t, x, epsilon = runrk(f,2,1,1.625,72)
#
#
#fig, (ax1,ax2) = plt.subplots(1,2)
#ax1.plot(t,x)
#ax2.plot(t,epsilon)
#ax2.set_title("Error")
#plt.show()
