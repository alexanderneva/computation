import numpy as np
import matplotlib.pyplot as plt
from horner import poly, evaluate

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
    points = np.zeros(n_step,dtype=float)

    for i in range(n_step):
        points[i] += x_0
        f_0 = f(x_0)
        f_prime_0 = f_prime(x_0)
        if np.abs(f(x_0))<alpha:
            print("Tolerance reached at step ",i)
            print("Value of root",np.round(x_0,5))
            return points[:i+1]
        elif np.abs(f_prime(x_0))<alpha:
            print('Step blow up')
            return 0
        x_0 -= f_0/f_prime_0
    print(f"{n_step} iterations reached")
    return points

def f(x):
    """
    Question 2 a) """
    return x**3-5*x**2-4*x+1

def f_prime(x):
    return 3*x**2 - 10*x -4


def phi(x):
    return x - 1/6 * f(x)


def iterate(f,x_0,n_step):
    """
    Recursively compose function f with itself n_step+1 times at x_0
    """
    if n_step == 0:
        return f(x_0)
    else:
        return f(iterate(f,f(x_0),n_step-1))


#points = newton(f,f_prime,[-1.,-0.5],15,1e-10)
##
#print(f"f(x_k) to 5 significant digits {f(-0.87527)}")
#f_coeffs = np.array([1,-5,-4,1])
#root = points[-1]
#print(points)
#iterate_root = iterate(phi,-0.75,15)
#
#f_1_root, f_2_coeffs = poly(f_coeffs,root)

#print(f_2_coeffs)
#f_2 = lambda x : f_2_coeffs[0]*x**2 + f_2_coeffs[1]*x + f_2_coeffs[2]
#f_2_prime = lambda x : 2*f_2_coeffs[0]*x + f_2_coeffs[1]
#
#
#points_2=newton(f_2,f_2_prime,[0,1],10,1e-10)
#root_2 = points_2[points_2 != 0][-1]
#
#points_3 = newton(f_2,f_2_prime,[5,6],10,1e-10)
#root_3 = points_3[points_3 != 0][-1]

#x = np.linspace(-1,7)
#plt.plot(x,f(x),label=f'f(x)')
#plt.plot(x,evaluate(f_2_coeffs,x),label=r'$f_2=\frac{f(x)}{x-\alpha}$')
#plt.plot(x,f_2_prime(x),label=r'$f_2^{\prime}$')
#plt.axhline(0,color='red')
#plt.axvline(root_2,color='purple')
#plt.text(
#    x=root_2,
#    y=3,
#    s=f' Root {np.round(root_2,5)}'
#)
#plt.axvline(root,color='indigo')
#
#plt.text(
#    x=root,
#    y=20,
#    s=f' Root {np.round(root,5)}'
#)
#plt.axvline(root_3,color='violet')
#plt.text(
#    x=root_3,
#    y=10,
#    s=f' Root {np.round(root_3,5)}'
#)
#plt.grid()
#plt.legend()
#plt.title(r"Roots of cubic $f(x) = x^3-5x^2-4x+1$")
#plt.tight_layout()
#plt.savefig('iterative_results/q2_roots.jpg',dpi=150)
#plt.show()


def bisection(f,I,n_step,tau):
    """
    Perform bisection on f on interval I for n_step at tolerance alpha
    """
    a = I[0]
    b = I[1]
    points = np.zeros((2,n_step))
    x_star = 0
    if np.sign(f(a))==np.sign(f(b)):
        print(f"f doesn't change sign on {a}, {b}")
        return 0
    for step in range(n_step):
        half_len = (b-a)/2
        x_star = a + half_len
        points[0,step] = a
        points[1,step] = b
        if half_len < tau:
            print(f'Tolerance {tau} reached at step {step}')

            points = points[:,:step]
            return x_star,points
        if np.sign(f(a))!= np.sign(f(x_star)):
            b = x_star
        else:
            a= x_star

    return x_star,points


def f(x):
    """
    Question 3
    """
    return np.cos(x)-2/3

#n_step = 15
#tau = 1e-3
#root, points = bisection(f,[0,np.pi/2],n_step,tau)
#
#step_stop=points.shape[1]
#steps = np.arange(step_stop)
#plt.plot(steps,points[1,:],'.',label='upper bound')
#plt.plot(steps,points[0,:],'.',label='lower bound')
#plt.fill_between(steps,points[0],points[1],alpha=0.2)
#plt.axhline(root,color='red',alpha=0.2)
#plt.text(
#    x = 1,
#    y = root,
#    s = f'Root at {np.round(root,3)}'
#)
#plt.xlabel('Steps')
#plt.legend()
#plt.grid()
#plt.title(rf'Bisection for $cos(x)-2/3$ on $[0,\pi/2]$ {'\n'} Steps {n_step} Tol {tau} at {step_stop+1}')
#plt.tight_layout
#plt.savefig('iterative_results/q3_bisection.jpg',dpi=150)
#plt.show()

def iterate_u(f,I,n_step,tau):
    """
    Tracking |x_{n-1}-x_n|< tau where tau is tolerance for the algorithm for maximum n_steps
    """
    x_0=np.mean(I)
    points = np.zeros(n_step,dtype=float)
    points[0]+=x_0
    for step in range(1,n_step):
        x = f(x_0)
        if np.abs(x_0-x) < tau:
            print(f'Tolerance {tau} reached at step {step}')
            points = points[:step]
            return points
        points[step] += x
        x_0 = x
    return points

def phi(x):
    """
    Question 3 b
    """
    return x + f(x)

#n_step = 15
#tau = 1e-3
#x_0 = 0
#points = iterate_u(phi,0,n_step,tau)
#root = points[-1]
#step_stop = points.shape[0]
#steps = np.arange(step_stop)
#plt.plot(steps,points)
#plt.title(rf"Successive sub. on $\phi(x) = x + f(x)$ {'\n'} at $x_0 = {x_0}$ Tol {tau} reached at step {step_stop}")
#plt.axhline(root,label=f'Root {root}',color='red',alpha=0.5)
#plt.text(
#    x = 0,
#    y = root,
#    s = f'Root at {np.round(root,3)}'
#)
#plt.grid()
#plt.tight_layout()
#plt.savefig('iterative_results/q3_substitution.jpg',dpi=150)
#plt.show()

def atiken(seq,tau):
    """
    Perform Atiken's method on n => 2 sequence seq. Quit when tolerance tau is reached for |x_n-x{n-1}|
    """
    n_points = seq.shape[0]-2
    points = np.zeros(n_points,dtype=float)
    for i in range(n_points):
        points[i] += seq[i] - (seq[i+1]-seq[i])**2 / (seq[i+2]-2*seq[i+1]+seq[i])
        if np.abs(points[i-1]-points[i]) < tau:
            print(f'Tolerance reached at step {i}')
            points = points[:i]
            return points
    return points

#print(atiken(points,tau))

def f_prime(x):
    """
    Question 3 d)
    """
    return -np.sin(x)

#print(newton(f,f_prime,[1,1],n_step,tau))

def newton_2(f,f_prime,I,n_step,tau):
    """
    Newton where tau controls |x_n-x_{n-1}|
    """
    points = np.zeros(n_step,dtype=float)
    x = np.random.uniform(I[0],I[1])
    for step in range(n_step):
        points[step] += x
        f_x = f(x)
        f_p = f_prime(x)
        mult = f_x / f_p
        x_0 = x
        x -= mult
        if np.abs(x-x_0)<tau:
            print(f"Tolerance {tau} reached at step {step}")
            return points[:step]
    return points

    

def check_convergence():
    """
    Check convergence on the bisection, successive sub., atiken's and newton's schemes. Using low tolerance newton as the benchmark for x_star
    """
    n_step = 50
    tau, tau_star = 1e-3, 1e-15
    I = [0,np.pi/2]
    x_star = newton_2(f,f_prime,[1,1],n_step,tau_star)
    x_star = x_star[-1]
    errors = np.zeros((4,n_step),dtype=float)
    _,test = bisection(f,I,n_step,tau)
    test_2 = iterate_u(phi,I,n_step,tau)
    test_3 = atiken(test_2,tau)
    test_4 = newton_2(f,f_prime,[1,1],n_step,tau)
    print(test_4)
    plt.plot(np.abs(np.mean(test,axis=0)-x_star),label='bisection')
    plt.plot(np.abs(test_2-x_star),label='successive substution')
    plt.plot(np.abs(test_3-x_star),label='atiken')
    plt.plot(np.abs(test_4-x_star),label='newton')
    plt.legend()
    plt.grid()
    plt.savefig('iterative_results/q3_errors.jpg',dpi=150)
    plt.show()
    return errors
#check_convergence()



def divided_difference(f,grid):
    """
    For function f return the divided difference f[x_0,...,x_k] for grid = {x_0,...,x_k}
    """
    if grid.size==0:
        return 0.
    if grid.size==1:
        return f(grid)

    elif grid.size == 2:
        return (f(grid[1])-f(grid[0]))/(grid[1]-grid[0])
    else:
        return (divided_difference(f,grid[1:]) - divided_difference(f,grid[:-1])) / (grid[-1]-grid[0])




def w_n(x,grid):
    """
    Return the function omega_n = (x-x_0)...(x-x_{n}) for value x
    """ 
    n = grid.shape[0]
    if n == 0:
        return np.ones_like(x,dtype=float)
    elif n == 1:
        return x - grid[0]
    else:
        return (x - grid[0])*w_n(x,grid[1:])


def plot_w(n=4):
    """
    Plot the polynomial omega_{k} for k <= n-1
    """
    grid = np.arange(n,dtype=float)
    test = lambda x,grid : w_n(x,grid)
    x = np.linspace(-1,4)
    fig, ax = plt.subplots(2,2,figsize=(13,8))
    ax = ax.flatten()
    for size,axs in enumerate(ax):
        axs.plot(x,test(x,grid[0:size+1]))
        for i,point in enumerate(grid[:size+1]):
            axs.axvline(point,color='orange',alpha=0.25)
            axs.axhline(0,color='red',alpha=0.25)
            axs.text(
                x = point,
                y = i,
                s = f"point {np.round(point,4)}"
            )
        axs.grid()

        axs.set_title(fr"$\omega_{size}(x)$")
    fig.suptitle(rf'first {n} $\omega_n$')
    plt.tight_layout()
    plt.savefig(f'iterative_results/w_{n-1}.jpg',dpi=150)
    plt.show()

def newton_term(f,x,grid,k):
    """
    Given a grid of n+1 points f(x_0),...,f(x_n), return the kth term of the interpolating polynomial of degree n
    """

    f_grid = grid[:k+1]
    w_grid = grid[:k]
    coeff = divided_difference(f,f_grid)
    wn = w_n(x,w_grid)
    
    return coeff*wn


def newton_interpolate(f,x,grid):
    """
    Given a grid of n+1 points f(x_0),...,f(x_n), return the interpolating polynomial of degree n
    """
    n = grid.shape[0] 
    sum = 0
    for k in range(n):
        sum += newton_term(f,x,grid,k)

    return sum

def plot_newton(n=6):
    """
    Plot first n interpolating polynomials
    """
    if n % 2 != 0 and n%3 != 0:
        return 0
    grid = np.arange(n,dtype=float)
    x = np.linspace(-1,n)
    fig,ax = plt.subplots(2,int(n/2),figsize=(13,8))
    for grid_v in range(n):
        ax = ax.flatten()
        ax[grid_v].plot(x,newton_interpolate(f,x,grid[0:grid_v+1]),label='p(x)',color='g')
        ax[grid_v].plot(x,f(x),label = 'f(x)')
        for point in grid[:grid_v+1]:
            ax[grid_v].axvline(point,color='red',alpha=0.25)
        ax[grid_v].set_ylim(-2,2)
        ax[grid_v].set_title(f"grid {grid[0:grid_v+1]}")
        ax[grid_v].legend()
        ax[grid_v].grid()
    fig.suptitle(rf"Polynom interpolation for $f(x)=\cos(x)-2/3$ {'\n'} on {grid}")
    plt.tight_layout()
    plt.savefig(f'iterative_results/newton_interp_{len(grid)}.jpg',dpi=150)
    plt.show()


#plot_newton(8)

from itertools import combinations

def lagrange_e(grid,k):
    """
    Using symbolic expression, given a grid of points, return the kth second order lagrange polynomial 
    """
    prim = '(x-)'
    omega_n = ''
    test = prim.find('-')
    x_k = prim[0:test+1]+str(grid[k])+prim[test+1:]
    print(x_k)
    print('old grid',grid)
    grid = np.delete(grid,k)
    print('new grid',grid)
    for val in grid:
        primm = prim
        omega_n += primm[0:test+1]+str(val)+primm[test+1:] + '*'
    omega_n = omega_n[0:-1]
    omega_n_p = ''
    if k > 2:
        for s,t in combinations(grid,2):
            primmm = prim
            print(s,t)
            omega_n_p += primmm[0:test+1]+str(s)+primmm[test+1:]+'*' +primmm[0:test+1]+str(t)+primmm[test+1:]+'+'
    if k <=2:
        for val in grid:
            primmm = prim
            omega_n_p += primmm[0:test+1]+str(val)+primmm[test+1:]+'+'
    omega_n_p = omega_n_p[0:-1]

    omega_n_p_k = omega_n_p+'*'+x_k
    x = np.linspace(-1,2)
    num = eval(omega_n)
    denom = eval(omega_n_p)
    return num / denom


def w_n_prime(x,grid):
    """
    Given a grid of points, return w_n'(x)
    """
    n = grid.shape[0]
    if n == 0:
        return np.zeros_like(x,dtype=float)
    if n == 1:
        return np.ones_like(x,dtype=float)
    else:
        x_n = grid[-1]
        grid = grid[:-1]
        if np.size(x)==1:
            return np.prod(x-grid)
        else:
            h_n = np.prod(x[:,None]-grid,axis=1)
        return h_n + (x-x_n)*w_n_prime(x,grid)



def plot_w_prime(n=4):
    """
    Plot the polynomial omega_{k}' for k <= n-1
    """
    if n % 2 != 0:
        print('Not divisible by 2')
        return 0
    grid = np.arange(n,dtype=float)
    test = lambda x,grid : w_n_prime(x,grid)
    x = np.linspace(-1,n)
    fig, ax = plt.subplots(2,2,figsize=(13,8))
    ax = ax.flatten()
    for size,axs in enumerate(ax):
        axs.plot(x,test(x,grid[0:size+1]))
        for i,point in enumerate(grid[:size+1]):
            axs.axvline(point,color='orange',alpha=0.5)
            axs.axhline(0,color='red',alpha=0.25)
            axs.text(
                x = point,
                y = i,
                s = f"point {np.round(point,4)}"
            )
        axs.grid()
        axs.set_title(fr"$\omega_{size}(x)$")
    fig.suptitle(rf'first {n} $\omega_n$')
    plt.tight_layout()
    plt.savefig(f'iterative_results/w_{n-1}_prime.jpg',dpi=150)
    plt.show()
    return 1

def lagrange(x,grid,k):
    """
    Return the kth lagrange polynomial 
    """
    x_k = grid[k]
    grid_k = np.delete(grid,k)
    l_nk = w_n(x,grid_k) / w_n_prime(x_k,grid)
    return l_nk

def lagrange_interpolate(f,x,grid):
    """
    Given a function f, and grid points grid, return the Lagrange interpolating polynomial L(x)
    """
    sum = 0.
    for k in range(len(grid)):
        sum += f(grid[k])*lagrange(x,grid,k)

    return sum




def plot_lagrange(n=6):
    """
    Plot first n interpolating polynomials
    """
    if n % 3 !=0 and n % 2 != 0:
        return 0
    grid = np.arange(n,dtype=float)
    x = np.linspace(-1,n)
    fig,ax = plt.subplots(2,int(n/2),figsize=(13,8))
    for grid_v in range(n):
        ax = ax.flatten()
        ax[grid_v].plot(x,lagrange_interpolate(f,x,grid[0:grid_v+1]),label='L(x)',color='g')
        ax[grid_v].plot(x,f(x),label = 'f(x)')
        for point in grid[:grid_v+1]:
            ax[grid_v].axvline(point,color='red',alpha=0.25)
        ax[grid_v].set_ylim(-2,2)
        ax[grid_v].set_title(f"grid {grid[0:grid_v+1]}")
        ax[grid_v].legend()
        ax[grid_v].grid()
    fig.suptitle(rf"Polynom interpolation for $f(x)=\cos(x)-2/3$ {'\n'} on {grid}")
    plt.tight_layout()
    plt.savefig(f'iterative_results/lagrange_interp_{len(grid)}.jpg',dpi=150)
    plt.show()
    return 1

plot_lagrange(6)
#grid = np.arange(4)
#x = np.linspace(-2,2)
##plt.plot(x,lagrange_interpolate(f,x,grid),label='L(x)')
#plt.plot(x,f(x),label='f(x)')
#plt.legend()
#plt.grid()
#plt.show()
