import numpy as np
import matplotlib.pyplot as plt



def bisection(f,a,b,n_step,eps):
    f_a = f(a)
    f_b = f(b)
    f_c = 0
    c = 0
    if np.sign(f_a) == np.sign(f_b):
        print(f"Same sign of function at [{a} , {b}]")
        return a,b,f_a,f_b
    error = b - a
    for i in range(n_step):
        error /= 2
        c = a + error
        f_c += f(c)
        if np.abs(error) < eps:
            return i,c,f_c,error
        if np.sign(f_a)!= np.sign(f_c):
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c
    return n_step,c,f_c,error


ticks = np.arange(0,0.01,10e-5)

steps = np.zeros(100)
errors = np.zeros(100)

def eval_bisection(f,a,b,n_steps):

    steps = np.zeros(n_steps)
    errors = np.zeros(n_steps)
    for i,j in enumerate(ticks):
        n_steps, c, f_c, error = bisection(f,a,b,n_steps//2,j)
        if n_steps == a:
            print("Same sign function")
            return 0
        else:
            steps[i] += n_steps
            errors[i] += error
    plt.plot(ticks,steps,label="Steps to converge")
    plt.plot(ticks,errors, label ="Convergence error")
    plt.title("Steps to converge")
    plt.legend()
    plt.show()
    return 0
    

def f(x):
    return x**2-3


#a_0 = f(0)
#print("a_0 ", a_0)
#a_1 = f(-a_0)-a_0
#print("a_1 ",a_1)
#a_2 = f(a_1)-a_1
#print("a_2 ", a_2)
#a_3 = f(-a_2)-a_2
#print("a_3 ", a_3)

#eval_bisection(f,-0.5,5,100)

def false_position(f,a,b,n_steps,eps):
    f_a = f(a)
    f_b = f(b)
    f_c = 0
    c = 0
    error = b - a
    if np.sign(f_a) == np.sign(f_b):
        print(f"Same sign of function at [{a} , {b}]")
        return a,b,f_a,f_b
    c += (a*f_b - b*f_a) / (f(b)-f(a))
    f_c += f(c)
    for i in range(n_steps):
        error /= 2
        c = a + error
        f_c += f(c)
        if np.abs(error) < eps:
            return i,c,f_c,error
        if np.sign(f_a)!= np.sign(f_c):
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c
    return c,f_c


def newton(f,f_prime,x,nmax,epsilon,delta):
    f_x = f(x)
    for n in range(nmax):
        f_p = f_prime(x)
        if f_p < delta:
            print("Small derivative ", f_p)
            return 0
        d = f_x / f_p
        x -= d
        f_x = f(x)
        if np.abs(d) < epsilon:
            print(f"Convergence at step {n}")
            return x,f_x
    return x,f_x


print(false_position(f,1,2,100,10e-5))
print(bisection(f,1,2,100,10e-5))


from math import cbrt

def f(x):
    return x**3 - 3

def f_p(x):
    return 3*x**2
ro, f_root = newton(f,f_p,1,100,10e-5,10e-5)

print(f"Root {ro}, f(root) {f_root} \n actual {cbrt(3)} relative error {(ro-cbrt(3))/cbrt(3)}")


from scipy.differentiate import jacobian

def system(u):
    t = u[0]
    x = u[1]
    y = u[2]
    return t*y+x, x**2-t*y, t*y**2


iv = np.array([-2.,2.,-1.])
def newton_rd_example(system,iv,n_step):
    m = iv.shape[0]
    points = np.zeros(shape=[m,n_step])
    x = iv.copy()
    for i in range(n_step):
        points[:,i] += x
        jac = jacobian(system, x)
        jac_matrix = jac.df
        h = np.linalg.solve(jac_matrix,system(x))
        #print(h)
        x -= h
    return x, points

#print(iv)
iv, points = newton_rd_example(system,iv,15)

ax = plt.figure().add_subplot(projection='3d')
ax.plot(points[:,0],points[:,1],points[:,2])
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y')
plt.show()
