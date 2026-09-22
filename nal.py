import numpy as np
#import matplotlib.pyplot as plt

n = 3
m = 3
X = np.random.uniform(size=(n,n))
#b = np.random.normal(size=n)

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

#print("A ", eg)
#print(f"a@x {eg@x}")
#print(f"a_r {a_r}")
#print(f"b {b}")
#print(f"b_r {b_r}")
#print(f"x {x}")


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
        for j in range(k,n):
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

def solve(a,b):
    # perform gaussian elimination and backsubstitutionproviding the reduced matrix a_r,b_r and solution vector x 
    a_r,b_r = gaussian_elim(a,b)
    x = backsub(a_r,b_r)
    return a_r,b_r,x

#a = np.array([
#    [0.0001,1],
#    [1,1]
#])
#b = np.array([1,2])

#
#a_r,b_r,x = solve(a,b)
#
#print(a_r)
#print(b_r)
#print(x)
#
def scaled_partial(x,b):
    # scaled partial pivoting
    a = x.copy()
    bb = b.copy()
    n , _  = np.shape(a)
    l = np.arange(n)
    s = np.zeros(n)
    for i in range(n):
        s_max = 0
        for j in range(n):
            s_max = np.max(np.array([s_max,np.abs(a[i,j])]))
        s[i] = s_max

    for k in range(n-1):
        r_max = 0
        for i in range(k,n):
            r = np.abs(a[l[i],k] / s[l[i]])
            if r > r_max:
                r_max = r
                j = i

        l[[k,j]] = l[[j,k]]

        for i in range(k+1,n):
            l_mult = a[l[i],k] / a[l[k],k]
#            a[l[i-1],k] = l_mult
            for j in range(k+1,n):
                a[l[i],j] -= l_mult*a[l[k],j]
            bb[l[i]] -= a[i,k]*b[l[k]]

    return a,bb


#print("A \n",eg) 
#ans,b_r = scaled_partial(eg,b)
#print(f"Scaled partial \n {ans} {b_r}")
##print(backsub(ans,b_r))


def tri(A,b):
    n, _ = np.shape(A)
    a = np.diag(A,k=-1)
    c = np.diag(A,k= 1)
    d = np.diag(A,k=0).copy()
    b = b.copy()
    x = np.zeros(n)
    for i in range(1,n):
        l = a[i-1]/d[i-1]
        d[i] -= l*c[i-1]
        b[i] -= l*b[i-1]
    x[n-1] =+ b[n-1]/d[n-1]
    for i in reversed(range(n-1)):
        x[i] = (b[i] - c[i]*x[i+1]) / d[i]

    return x



A = np.array([
    [1,2,0],
    [2,2,4],
    [0,3,6]
])

b = np.array([1,0,2])

ans = tri(A,b)
test = np.linalg.solve(A,b)

print(f"Answer {ans}")
print(f"abs error {np.abs(ans-test)}")


#########

import scipy as sci
l, u = lu(A)
l_test,u_test = sci.linalg.lu(A, permute_l=True)

print(l_test@u_test)
print(np.abs(l-l_test))
print(np.abs(u-u_test))
print(l@u)

def doolittle(A):
    a = A.copy()
    n,_ = np.shape(A)
    l = np.eye(n)
    u = np.zeros_like(A,dtype=float)

    for k in range(n):
        for j in range(k,n):
            u[k,j] = a[k,j] - l[k,:]@u[:,j]
        for i in range(k+1,n):
            l[i,k] = (a[i,k] - l[i,:]@u[:,k]) / u[k,k]
    return l,u


def l_solve(L,b):
    n = L.shape[0]
    z = np.zeros(n)
    z[0]=b[0]
    for i in range(1,n):
        z[i] = b[i] - L[i,:]@z
    return z

def u_solve(U,z):
    n = U.shape[0]
    x = np.zeros(n)
    x[n-1] = z[n-1] / U[n-1,n-1]
    for i in reversed(range(n)):
        x[i] = (z[i] - U[i,i+1:]@x[i+1:]) / U[i,i]
    return x


def lu_solve(A,b):
    l,u = doolittle(A)
    z = l_solve(l,b)
    x = u_solve(u,z)
    return x

#l,u = doolittle(A)
#print("Difference ", lu_solve(l,b)-np.linalg.solve(A,b))
#
def make_spd(n):
    M = np.random.randn(n,n)
    spd = M@M.T + n*np.eye(n)
    return spd


A = make_spd(n)

def cholesky(A):
    a = A.copy()
    n = A.shape[0]
    l = np.zeros_like(A,dtype=float)
    for k in range(n):
        value = a[k,k] - l[k,:k]@l[k,:k]
        l[k,k] = np.sqrt(value)
        for i in range(k+1,n):
            l[i,k] = (a[i,k] - l[i,:k]@l[k,:k]) / l[k,k]
    return l

print(np.round(A,2))
l = cholesky(A)
print(np.round(l,2))
print(l@l.T-A)

def cholesky_solve(A,b):
    a = A.copy()
    l = cholesky(a)
    z = l_solve(l,b)
    x = u_solve(l.T,z)
    return x


B = make_spd(n)

def big_solve(A,B):
    x = np.zeros_like(A,dtype=float)
    n = A.shape[0]
    for i in range(n):
        _,_,x_i = solve(A,B[:,i])
        #x_i = lu_solve(A,B[:,i])
        #x[:,i]+= lu_solve(A,B[:,i])
        x[:,i]+= x_i
    return x

X = big_solve(A,B)
print("B",B)
print("X",X)
print("AX",A@X)

print("Difference big_solve X - np.linalg X \n", np.round(X - np.linalg.solve(A,B),5))


inverse = big_solve(A,np.eye(A.shape[0]))
#print(np.round(A@inverse,5))

### Adams-Bashforth-Moulton

def adams_bash(n):
    """Return Adams-Bashforth-Moulton solution of size n"""
    b = np.zeros(n)
    A = np.zeros(shape=(n,n))
    for i in range(1,n+1):
        b[i-1]= 1 / i
        for j in range(n):
            A[i-1,j] += (1-j)**(i-1)


    A_r,b_r,x = solve(A,b)
    return x


eg = np.array([
    [1, 2, -1],
    [2, 5,  0],
    [3, 2, -1],
])

b = np.array([2,2,4])

eig_vals,eig_vects = np.linalg.eig(eg)
eig_vals = np.real(eig_vals)

_,_,x = solve(eg,b)


def hilbert(n):
    """Generate an n x n Hilbert matrix"""
    A = np.zeros(shape=(n,n))
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1,j-1] = 1 / (i + j -1)
    return A

def iterative(A,b,error=0.1,step=0):
    n = A.shape[0]
    omega = 1e-5
    #B = make_spd(n)
    #B =   (1  / np.diag(A) )
    B = omega*np.eye(n)
    Q = np.eye(n) - B@A
    guess = np.random.normal(size=(n,))
    err = []
    err_0 = np.linalg.norm(guess-x)
    err.append(err_0)
    k = 0
    while err_0 > error:
        B = omega*l
        Q = np.eye(n) - B@A
        if k % 100 == 0 and k >0:
            print("Step ", k)
            print("Spec radius of Q", np.linalg.norm(Q,2))
            err_0 = np.linalg.norm(guess-x)
            return guess,err
        guess = Q@guess + B@b
        err_0 = np.linalg.norm(guess-x)
        k += 1
        omega += 1e-5
    return guess,err


guess, err = iterative(eg,b,error=0.75)
print(guess, err[-1])
print("Relative error ", err[-1]/np.linalg.norm(x))



