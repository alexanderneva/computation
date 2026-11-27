import numpy as np
from nal import solve,hilbert,cholesky,big_solve,lu_solve,cholesky_solve

A = hilbert(5)
l = cholesky(A)
print(np.round(l,6))
print(np.round(l@l.T-A,2))

l_inv = big_solve(l,np.eye(5))

print("Inf Norm of l_inv ", np.linalg.norm(l,np.inf))

print("Inf Norm of A", np.linalg.norm(A,np.inf))


A_inv = big_solve(A,np.eye(5))


print("Inf Norm of A inv", np.linalg.norm(A_inv,np.inf))

b = np.array([
    5, 3.55, 2.81428571428571,2.34642857142857,
    2.01746031726032
]
             )

A_r,b_r,x_1 = solve(A,b)

x_1_l = lu_solve(A,b)

x_1_chol = cholesky_solve(A,b)


print("LU solve ", x_1_l)
print("Chol solve ", x_1_chol)
print("Standard gaussian elim ", x_1)
A_tilde = A.copy()
A_tilde[4,0] = 0.20001
A_tilde_inv = big_solve(A_tilde,np.eye(5))

print("Inf Norm of A_~ ", np.linalg.norm(A_tilde,np.inf))
print("Inf Norm of A_~_inv ", np.linalg.norm(A_tilde_inv, np.inf))

_,_,x_2 = solve(A_tilde,b)
x_2_l = lu_solve(A_tilde,b)
x_2_chol = cholesky_solve(A_tilde,b)

print(x_1_chol - x_2_chol)
print("Norm of x_1 - x_2", np.linalg.norm(x_1-x_2,np.inf))
print("Norm of x_l_1 - x_l_2", np.linalg.norm(x_1_l-x_2_l,np.inf))
print("Norm of x_1_chol - x_2_chol", np.linalg.norm(x_1_chol-x_2_chol,np.inf))
print("Norm of x_1", np.linalg.norm(x_1))
print("Norm of x_1_l", np.linalg.norm(x_1_l))
print("Norm of x_1_chol", np.linalg.norm(x_1_chol))



print("A Standard Gaussian error: ", np.linalg.norm(A@x_1-b))
print("A LU solve error: ", np.linalg.norm(A@x_1_l-b))
print("A Cholesky error: ", np.linalg.norm(A@x_1_chol-b))


print("A_~ Standard Gaussian error: ", np.linalg.norm(A_tilde@x_2-b))
print("A_~ LU solve error: ", np.linalg.norm(A_tilde@x_2_l-b))
print("A_~ Cholesky error: ", np.linalg.norm(A_tilde@x_2_chol-b))
