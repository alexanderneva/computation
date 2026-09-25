import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

expr_1 = 't+np.exp(-2*t)-3*y'
expr_2 = '1 + t*np.exp(-t) - y'
expr_3 = '3+2*np.cos(2*t)-1/4 *y'
expr_4 = '3*np.cos(2*t)-(1/t)*y'

def evaluator_1(t,y,expr):
    """Expression evaluator for first order ODE"""
    return eval(expr)
def solution_1(t,c):
    return t/3 -1/9 + np.exp(-2*t)+c*np.exp(-3*t)

def solution_4(t,c):
    return 3/2 *(np.sin(2*t)+np.cos(2*t)/2/t)
def plot_field(expr,index):
    """Convert a functional first order ODE expression into vector field plot"""
#    q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
    t_max = 9
    time = np.linspace(-1,t_max,25)
    space = np.linspace(-5,5,25)
    I, J = np.meshgrid(time,space)
    fig, ax = plt.subplots()

    U = np.ones_like(I)
    V = evaluator_1(I,J,expr)
    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
    q = ax.quiver(I,J,U,V,scale=10,angles='xy',scale_units='xy',pivot='mid')
    ax.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='E')
    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
    cs = np.arange(-5,5,1)
    for c in cs:
        for t0 in np.arange(0.1,5,5):
            y0 = c
            sol = solve_ivp(lambda t,y : evaluator_1(t,y,expr),(t0,t_max),[y0])
            ax.plot(sol.t,sol.y[0],label='Soln at y0 = '+str(c))
            ax.plot(time,solution_4(time,y0))
    ax.set_aspect('equal')
    ax.set_ylim(-5,5)
    plt.title(f"Equation u_1 = {expr} \n")
    plt.tight_layout()
    plt.savefig(f'fields/field_exercise_{index}.jpg')

    plt.show()

plot_field(expr_4,4)
