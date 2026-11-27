import numpy as np
import matplotlib.pyplot as plt
from horner import poly, evaluate,evaluate_f

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
#l,u = take_ul(A)

from nal import lu
A = np.array([[2,1,4,5],
             [3,-1,1,2],
             [2,3,-2,-3],
             [1,-5,3,6]])

#l,u = lu(A)
#
#print(l)
#print(u)

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
        return f(grid.item())

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


def newton_term_2(f,x,grid,k):
    """
    Given a grid of n+1 points f(x_0),...,f(x_n), return the product elements of the kth term of the degree n newton polynomial
    """

    f_grid = grid[:k+1]
    w_grid = grid[:k]
    coeff = divided_difference(f,f_grid)
    wn = w_n(x,w_grid)
    
    return coeff,w_n


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
    denom = w_n(x_k,grid_k)
    l_nk = np.divide(w_n(x,grid_k),denom, out = np.ones_like(x,dtype=float), where = denom!=0)
    return l_nk

def lagrange_interpolate(f,x,grid):
    """
    Given a function f, and grid points grid, return the Lagrange interpolating polynomial L(x)
    """
    sum = 0.
    for k in range(len(grid)):
        sum += f(grid[k])*lagrange(x,grid,k)

    return sum


def plot_lagrange_polynomials(n=4):
    """
    Plot the n degree Lagrange polynomials for grid {x_0,...x_{n+1}
    """

    grid = np.arange(n,dtype=float)
    test = lambda x,grid,k : lagrange(x,grid,k)
    x = np.linspace(-1,4)
    fig, ax = plt.subplots(2,2,figsize=(13,8))
    ax = ax.flatten()
    for size,axs in enumerate(ax):
        axs.plot(x,test(x,grid,size))
        for i,point in enumerate(grid):
            axs.axvline(point,color='orange',alpha=0.25)
            axs.axhline(0,color='red',alpha=0.25)
            axs.text(
                x = point,
                y = i,
                s = f"point {np.round(point,4)}"
            )
        axs.grid()
        axs.set_title(fr"$L{({n-1},{size})}\left(x\right)$")
    fig.suptitle(rf'Lagrange polynomials $L_{n-1}$')
    plt.tight_layout()
    plt.savefig(f'iterative_results/L_{n-1}.jpg',dpi=150)
    plt.show()

#plot_lagrange_polynomials()

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

#plot_lagrange(6)

def calculate_mse(x,y):
    """
    Take the MSE of two functions x and y
    """
    return np.sqrt((x-y)**2)

#grid = np.arange(5)
#x = np.linspace(0,4)
#plt.plot(x,calculate_mse(f(x),lagrange_interpolate(f,x,grid)),label='lagrange')
#plt.plot(x,calculate_mse(f(x), newton_interpolate(f,x,grid)),label='newton')
#plt.grid()
#plt.legend()
#plt.title(f'MSE newton/lagrange polynomial for grid {grid}')
#plt.savefig(f'iterative_results/mse_lagrange_newton_interp_{len(grid)}.jpg',dpi=150)
#plt.show()

def runge(x):
    """
    Runge function
    """
    mask = lambda x : np.where(x,0,x < -1 or x > 1)
#    print(x[x > 1])

    return 1/(1+25*x**2)


def c_grid(n):
    """
    Return a chebyshev grid on lb,ub of n points
    """
    z = np.zeros(n,dtype=float)
    for k in range(n):
        z[k] = np.cos((2*k+1)*np.pi/(2*(n+1)))
    return z


n=12
lb = -1.
ub = 1.
grid = np.arange(-1,1,2/n)
x = np.linspace(lb,ub)


coeffs = np.zeros(n,dtype=float)
for i in range(n):
    coeff,_ = newton_term_2(f,x,grid,i)
    coeffs[i] = coeff


print(c_grid(n))
cgrid = c_grid(n)

print(f"Coefficients of {n} order newton polynomial {np.round(coeffs,6)}")
def plot_runge():
    fig, ax = plt.subplots(1,2,figsize=(8,5))
    ax[0].plot(x,lagrange_interpolate(runge,x,grid),label='Runge function Lagrange interpolation')
    ax[0].plot(x,newton_interpolate(runge,x,grid),label='Runge function Newton interpolation')
    ax[0].plot(x,runge(x), label='Runge function')
    #plt.plot(x,w_n(x,grid),label='w_n')
    ax[0].scatter(grid,runge(grid),label='Sample points',c='green',alpha=0.5)
    ax[0].set_ylim(-1,1)
    ax[0].set_title(fr"Runge Function on $\Delta$ ,{'\n'} lb = {lb} ub = {ub}")

    ax[1].plot(x,lagrange_interpolate(runge,x,cgrid),label='Runge function Lagrange interpolation')
    ax[1].plot(x,newton_interpolate(runge,x,cgrid),label='Runge function Newton interpolation')
    ax[1].plot(x,runge(x), label='Runge function')
    #pl1.plot(x,w_n(x,grid),label='w_n')
    ax[1].scatter(cgrid,runge(cgrid),label='Sample points',c='green',alpha=0.5)
    ax[1].set_ylim(-1,1)
    plt.legend()
    ax[1].set_title(fr"Runge Function on Grid $\Delta_C$ ,{'\n'} lb = {lb} ub = {ub}")
    fig.suptitle("Runge function even grid vs. chebyshev grid")
    fig.tight_layout()
    plt.savefig(f'iterative_results/runge_interp_uni_chebi_grid_{len(grid)}.jpg',dpi=150)
    plt.show()

    x = np.linspace(-1,1)
    plt.plot(x,calculate_mse(runge(x),lagrange_interpolate(runge,x,grid)),label='lagrange')
    plt.plot(x,calculate_mse(runge(x), newton_interpolate(runge,x,grid)),label='newton')

    plt.plot(x,calculate_mse(runge(x),lagrange_interpolate(runge,x,cgrid)),label='lagrange c_grid')
    plt.plot(x,calculate_mse(runge(x), newton_interpolate(runge,x,cgrid)),label='newton c_grid')
    plt.grid()
    plt.ylim(0,2)
    plt.legend(loc='center')
    plt.title(f'MSE newton/lagrange polynomial for grid {len(grid)}\n chebyshev grid {len(cgrid)}')
    plt.savefig(f'iterative_results/mse_ln_runge_interp_{len(grid)}.jpg',dpi=150)
    plt.show()

def lagrange_interpolate_data(data,x):
    """
    Given data of the form
    (x,f(x)) : (n,2) array,
    produce the lagrange interpolating polynomial
    """
    f = data[:,1]
    grid = data[:,0]
    sum = 0
    for k in range(len(grid)):
        sum += f[k]*lagrange(x,grid,k)
    return sum

    

def experiment_1(n):
    """
    Return the lagrange interpolating polynomial on random data of length n
    """
    toy_graph = np.array([[0,1],
                         [1,-1],
                          [2,0],
                          [3,1],
                         [4,-1],
                         [5,0]])

    fs = np.random.normal(loc=1,scale=0.5,size=(n,))
    xs = np.arange(0,n)
    toy_graph = np.column_stack([xs.T,fs.T])
    print(fs.T)
    print(xs.T)
    print(toy_graph.shape)
    x = np.linspace(0,n)
    plt.plot(x,lagrange_interpolate_data(toy_graph,x),label='interpolating polynomial')
    plt.plot(toy_graph[:,0],toy_graph[:,1],'.',color='red',label='data')
    plt.ylim(-3,3)
    plt.legend()
    plt.title(f"Lagrange polynomial on random data of shape {toy_graph.shape}")
    plt.show()
    return 1



graph = np.array([[-1,13],
                  [0,7],
                 [1,9]])

#experiment_1(20)
def forward_difference(seq,k,index):
    """
    For a sequence seq of points, return the k-th order forward difference at index
    """
    if k ==0:
        return 1
    elif type(seq)==np.int64:
        return 0
    elif k > len(seq):
        return 0

    elif 0<=index and k+index < len(seq)-1:

        if k == 1:
            delta = seq[index+1] - seq[index]
            seq[index] = delta
            return delta
    #    if k <= 2 and k <=index+1:
    #        return seq[index+1]-seq[index]
        else:
            delta_1 = forward_difference(seq,1,index+1)
            delta_2 = forward_difference(seq,1,index)
            delta = delta_1-delta_2
            return forward_difference(delta,k-1,index)
#            return forward_difference(forward_difference(seq,k-1,index),1,index)
    else:
        print("Index out of bounds")
        return 0

def forward_difference(seq,k):
    L = len(seq)
    if L == 0:
        return seq
    elif L == k:
        return seq
    else:
        new = seq[:-1]
        for i in range(L-1):
            new[i] = seq[i+1]-seq[i]
        return forward_difference(new,k)


for i in range(17):
    seq = np.arange(16)
    print(f"Forward difference {i} ", forward_difference(seq,i))
#print(seq)
x0 = np.repeat(1,2)
x1 = np.repeat(2,3)
x2 = np.array([3])
grid = np.concatenate([x0,x1,x2])
#print(grid)
f = lambda x : np.exp(x)

