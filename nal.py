import numpy as np
#import matplotlib.pyplot as plt

n = 3
m = 3
X = np.random.uniform(size=(n,n))
b = np.random.normal(size=n)

eg = np.array([
    [1, 2, -1],
    [2, 5,  0],
    [3, 2, -1],
])

b = np.array([2,2,4])

def forward_sub(A):
    # gaussian forward substitution
    a = np.copy(A)
    n,_ = np.shape(a)
    l = np.zeros_like(a)
    for k in range(n):
        for i in range(k+1,n): 
            l[i-1,k] += a[i,k] / a[k,k]
            for j in range(k,n):
                a[i,j] -= l[i-1,k]*a[k,j]
    return a


def gaussian_elim(A,b):
    a = np.copy(A)
    n,_ = np.shape(a)
    bb = b.copy()
    l = np.zeros_like(a)
    for k in range(n):
        for i in range(k+1,n): 
            l[i-1,k] += a[i,k] / a[k,k]
            for j in range(k,n):
                a[i,j] -= l[i-1,k]*a[k,j]
            bb[i] -= l[i-1,k]*bb[k]
    print("b_r", bb)
    return a,bb

def backsub(A,b):
    a = np.copy(A)
    n = np.size(b)
    x = np.zeros(n)
    x[n-1] = b[n-1] / a[n-1,n-1]
    for i in reversed(range(n)):
        sum = b[i]
        for j in range(i+1,n):
            sum -= a[i,j]*x[j]
        x[i] = sum/a[i,i]
    return x


a_r,b_r = gaussian_elim(eg,b)
np.round(a_r,2)
x = backsub(a_r,b_r)

print("A ", eg)
print(f"a@x {eg@x}")
print(f"a_r {a_r}")
print(f"b {b}")
print(f"b_r {b_r}")
print(f"x {x}")


def gaussian_elim_mult(A,b):
    a = np.copy(A)
    n = np.size(b)
    bb = b.copy()
    for k in range(n+1):
        for i in range(k,n):
            xmult = a[i,k] / a [k,k]
            a[i,k] = xmult
            for j in range(k+1,n):
                a[i,j] = a[i,j] - xmult*a[k,j]
            bb[i] -= xmult*b[k]
    return a,bb




def lu(x):
    a = x.copy()
    n,_ = np.shape(a)
    l = np.zeros_like(a)
    u = np.zeros_like(a)
#    u = forward_sub(x)
    for k in range(n):
        l[k,k] = 1
        u[k,k] = a[k,k] - l[k,:k] @ u[:k,k]
        print(f" u {k} {u}")
        for j in range(k,n):
            print(f" j {j}")
            u[k,j] = (a[k,j] - l[k,:k] @ u[:k,j]) 
        for i in range(k,n):
            l[i,k] = (a[i,k] - l[i,:k] @ u[:k,k]) / u[k,k]
    return l,u

def lu_with_forward(x):
    a = x.copy()
    n,_ = np.shape(a)
    l = np.zeros_like(a)
    u = forward_sub(a)
    for k in range(n):
        l[k,k] = 1
        for i in range(k,n):
            l[i,k] = (a[i,k] - l[i,:k] @ u[:k,k]) / u[k,k]
    return l,u

print(f'A {eg}')


l,u = lu(eg)


print(f' L \n {l}')
print(f' U \n {u}')
print(f' L@U \n {np.round(l@u,3)}')
print(f' A - L@U \n {np.round(eg - l@u)}')

l,u = lu_with_forward(eg)


print(f' L \n {l}')
print(f' U \n {u}')
print(f' L@U \n {np.round(l@u,3)}')
print(f' A - L@U \n {np.round(eg - l@u)}')

