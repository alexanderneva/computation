import numpy as np
#import matplotlib.pyplot as plt

n = 3
m = 3
X = np.random.uniform(size=(n,n))
b = np.random.normal(size=n)

def gaussian_elim(A,b):
    a = np.copy(A)
    n,_ = np.shape(a)
    bb = b.copy()
    print(f"b {b}") 
    for k in range(n):
        for i in range(k+1,n):
            for j in range(k,n):
                a[i,j] = a[i,j]-(a[i,k]/a[k,k])*a[k,j]
                #print(f"A {i} {j} {a[i,j]}")
            print("bb",  bb)
            bb[i] = bb[i] - (a[i,k] / a[k,k])*bb[k]
            print(f"b {i} {bb[i]} {bb}")
    print("b_r", bb)
    return a,bb

a_r,b_r = gaussian_elim(X,b)
np.round(a_r,2)
#x = backsub(a_r,b_r)

print("A ", X)
#print(f" a_r@x {a_r@x}")
#print(f"a@x {X@x}")
print(f"A_r {a_r}")
print(f"b {b}")
print(f"b_r {b_r}")

def myfunc():
    b = np.random.normal(size=3)
    a = b.copy()
    a[0]=100
    print(b,a)
    return b,a

#myfunc()

def gaussian_elim_mult(A,b):
    a = np.copy(A)
    n = np.size(b)
    for k in range(n+1):
        for i in range(k,n):
            xmult = a[i,k] / a [k,k]
            a[i,k] = xmult
            for j in range(k+1,n):
                a[i,j] = a[i,j] - xmult*a[k,j]
            b[i] -= xmult*b[k]
    return a,b

def backsub(A,b):
    a = np.copy(A)
    n = np.size(b)
    x = np.zeros(n)
    x[n-1] = b[n-1] / a[n-1,n-1]
    for i in reversed(range(n)):
        sum = b[i]
        for j in range(i,n):
            sum -= sum - a[i,j]*x[j]
        x[i] = sum/a[i,i]
    return x



def lu(x):
    a = np.copy(x)
    n,_ = np.shape(a)
    l = np.zeros_like(a)
    u = np.zeros_like(a)
    for k in range(n):
        l[k,k] = 1
        u[k,k] = a[k,k] - np.dot(l[k,0:k],u[0:k,k]) 
        for j in range(k,n):
            u[k,j] = (a[k,j] - np.dot(l[k,0:k],u[0:k,k])) / l[k,k]
        for i in range(k,n):
            l[i,k] = (a[i,k] - np.dot(l[i,0:k],u[0:k,k])) / u[k,k]

    return l,u


#print(f'A {X}')

#print(f"determinant {np.linalg.det(X)}")

#l,u = lu(X)
#
#print(f' L \n {l}')
#print(f' U \n {u}')
#print(f' L@U \n {np.round(l@u,3)}')
#print(f' A \n {np.round(X,3)} ')
#print(f' A - L@U \n {np.round(X - l@u)}')
