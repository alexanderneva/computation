import numpy as np
import matplotlib.pyplot as plt


def moment_test(f,max_step):
    """Simple test for highest x term"""
    n = max_step

    t = np.arange(0,50)
    f_min = np.min(f(t))
    max_errors=np.zeros(n)
    for j in range(n):

        deg = j
        x = np.zeros(50)
        for i in range(1,50):
            x[i] += f(i)/i**j-1

        max_error = np.max(x)
        max_errors[j]+=max_error
        if max_error == np.min(max_errors[j-1]):
            deg = j-1

            print("Max error reached at step", deg)
            return deg

        #print(f"Max error {np.max(x)} Average Error {np.mean(x)}")
        print(f"Max errors {max_errors}")
        plt.plot(t, x)
        plt.title(f"Moment for exponent {j}")
        plt.show()

    return deg


def f(x):
    return x**9+1

print("Moment test ", moment_test(f,13))

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
    return np.sin(x**2)
eval_bisection(f,-0.5,5,100)
#a_0 = f(0)
#print("a_0 ", a_0)
#a_1 = f(-a_0)-a_0
#print("a_1 ",a_1)
#a_2 = f(a_1)-a_1
#print("a_2 ", a_2)
#a_3 = f(-a_2)-a_2
#print("a_3 ", a_3)



    #        print(f"Max error {np.max(x)} Average Error {np.mean(x)}")
    #        plt.plot(t, x)
    #        plt.title(f"Moment for exponent {j}")
    #        plt.show()

#m = moment_test(f,25)
#print(m)

    #def coeffs(f):
    #    l = moment_test(f,5)
    #    a = np.zeros(5)
    #    a[0] = f(0)
    #    for i in range(1,5):
    #        a[i] += f((-1)**i * a[i-1]) - a[i-1]
    #    return a 

#print(bisection(f,-1,1,100,0.001))
#print(np.roots(np.array([1,-1,1,-1])))
