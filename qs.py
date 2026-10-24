import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1,2,3],
    [5,8,2],
    [-1,2,1]
],dtype=float)

B = np.array([
    [1,0,3],
    [7,-5,2],
    [1,1,-2]
],dtype=float)

def mult(A,B):
    """
    Matrix multiplication on A: pxm B: mxn 
    """
    if A.shape[1]!=B.shape[0]:
        print("Shape mismatch")
        return 0
    p = A.shape[0] 
    n = B.shape[1]
    index_a = np.arange(A.shape[0])
    index_b = np.arange(B.shape[1])
    c = np.zeros(shape=(p,n),dtype=float)
    for i in index_a:
        for j in index_b:
            c[i,j] = A[i,:]@B[:,j]
    return c

def take_ul(A):
    """Return the lower and upper triangular portions of A"""
    l = np.zeros_like(A,dtype=float)
    u = np.zeros_like(A,dtype=float)
    n = A.shape[0]
    if n!=A.shape[1]:
        print("The matrix isn't square")
        return 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                u[i,j]+= A[i,j]
    l = A - u + np.diag(A)*np.eye(n)
    return l,u


def take_l(A):
    """Take the lower triangular portion of A"""
    c = np.zeros_like(A,dtype=float)
    n = A.shape[0]
    if n!=A.shape[1]:
        print("The matrix isn't square")
        return 0
    for i in range(n):
        for j in range(n):
            if j <= i:
                c[i,j]+= A[i,j]
    return c
#print(mult(A,B))
#print(A@B)
l,u = take_ul(A)


def newton(f,f_prime,I,n_step,alpha):
    """
    Perform newton's method on function f with derivative f prime starting at point x_0 random in interval I for n_step iterations to tolerance np.abs(f(x_k))<alpha
    """
    x_0 = np.random.uniform(I[0],I[1])
#    x_0 = 0.75
    points = np.zeros(n_step,dtype=float)
    for i in range(n_step):
        points[i] += x_0
        f_0 = f(x_0)
        f_prime_0 = f_prime(x_0)
        if np.abs(f(x_0))<alpha:
            print("Tolerance reached at step ",n_step)
            print("Value of root",np.round(x_0,5))
            return points
        elif np.abs(f_prime(x_0))<alpha:
            print('Step blow up')
            return 0
        x_0 -= f_0/f_prime_0
    print(f"{n_step} iterations reached")
    return points

def f(x):
    """
    Question 2 a)
    """
    return x**3-5*x**2-4*x+1

def f_prime(x):
    return 3*x**2 - 10*x -4

points = newton(f,f_prime,[-1.,-0.5],10,1e-10)

print(f"f(x_k) to 5 significant digits {f(-0.87527)}")

def phi(x):
    return x - 1/6 * f(x)


def iterate(f,x_0,n_step):
    """
    compose function f with itself n_step+1 times at x_0
    """
    if n_step == 0:
        return f(x_0)
    else:
        return f(iterate(f,f(x_0),n_step-1))

print(iterate(phi,-0.75,20))
