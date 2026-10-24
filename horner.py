import numpy as np

def poly(a,x):
    """
    Horner's algorithm and return q(x)=b_{n-1}x^{n-1}+...+b_0 s.t
    p(x) = (x-a)q(x)+p(a)
    """
    p = a[0]
    b = np.zeros(a.size-1)
    for i in range(1,a.size):
        #        print('p',p)
        #        print('index', i, 'coeff',a[i])
        b[i-1] += p
        p = a[i] + x*p

    return p,b

def evaluate(a,x):
    """
    Descending evaluate a polynomial at point x with coeficients a
    """
    total = 0
    num_coeffs = a.size
    for i,j in enumerate(a):
        total += j*x**(num_coeffs-1-i)
    return total


def evaluate_f(a,x):
    """
    Ascending evaluate a polynomial at point x with coeficients a
    """
    total = 0
    for i,j in enumerate(reversed(a)):
        total += j*x**(i)
    return total

a = np.array([3,-7,-5,1,-8,2])
x = 4

#print(evaluate(a,x))
#print(evaluate_f(a,x))
#
#print(poly(a,x))

#for i in range(2):
#    for j in range(2):
#        for k in range(2):
#            print(f"Polynomial of index {i} {j} {k} Answer: {poly(np.array([i,j,k]),3)}")
#

