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

print(false_position(f,1,2,100,10e-5))
print(bisection(f,1,2,100,10e-5))



