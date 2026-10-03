import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# exercises from boyce + diprima

expr_1 = 't+np.exp(-2*t)-3*y'
expr_2 = '1 + t*np.exp(-t) - y'
expr_3 = '3+2*np.cos(2*t)-1/4 *y'
expr_4 = '3*np.cos(2*t)-(1/t)*y'
expr_5 = '(t-np.exp(-t))/(y+np.exp(y))'
expr_6 = 't**2 / (1+y**2)'
expr_7= 'y'
expr_8='-t'
expr_9='-t*np.exp(t)/y'
expr_10 = '2*t/(1+2*y)'
expr_11 = 'np.sin(2*y)/np.cos(3*t)'
expr_12 = '3*t**2 / (3 *y**2 - 4)'
expr_13 = '(y - 4*t) / (t-y)'
expr_14 = '(t**2 + t*y + y**2 )/ t**2'
expr_15 = '(t**2 + 3*y**2)/(2*t*y)'
expr_16 = 'y*(1-2*y)'
expr_17 = 'y+y**2'
expr_18 = 'y*(y-1)*(y-2)'
expr_19 = 'np.exp(y) -1'
expr_20 = '-2*np.arctan(y) / (1 + y**2)'
expr_21 = '-2*(y-1)**2'
expr_22 = 'y**2*(y**2-1)'
expr_23 = '0.5*y - np.sqrt(y)'
expr_24 = '0.025*y*np.log(2/y)'
expr_list = [expr_1,expr_2,expr_3,expr_4,expr_5,expr_6,expr_7,expr_8,expr_9,expr_10,expr_11,expr_12,expr_13,expr_14,expr_15]

def evaluator_1(t,y,expr):
    """Expression evaluator for first order ODE"""
    return eval(expr)

def evaluator_2(x,Y,expr_1,expr_2):
    t = Y[0]
    y = Y[1]
    return [eval(expr_1),eval(expr_2)]

def solution_1(t,c):
    return t/3 -1/9 + np.exp(-2*t)+c*np.exp(-3*t)

def solution_4(t,c):
    return 3/2 *(np.sin(2*t)+np.cos(2*t)/2/t)

def zero_event(t,y):
    return abs(y[0])-1e-3
def plot_field(expr,index):
    """Convert a functional first order ODE expression into vector field plot"""
#    q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
    t_max = 10
    t_min = 0
    time = np.linspace(t_min,t_max,25)
    space = np.linspace(0,6,25)
    I, J = np.meshgrid(time,space)
    fig, ax = plt.subplots()
    U = np.ones_like(I)
    V = evaluator_1(I,J,expr)
    V = np.where(V!=0, V, np.nan)
    length = np.hypot(U,V)
    #V = J
#    U,V=evaluator_2(I,J,expr_7,expr_8)
    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
    q = ax.quiver(I,J,U / length,V / length,scale=10,angles='xy',scale_units='xy',pivot='mid')
    ax.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='E')
    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
    cs = np.arange(0,6,0.25)
    for c in cs:
        for t0 in np.arange(t_min,t_max,1):
            y0 = c
            zero_event.terminal = True
            sol = solve_ivp(lambda t,y : evaluator_1(t,y,expr),(t0,t_max),[y0],events=zero_event)
            ax.plot(sol.t,sol.y[0],label='Soln at t0 = '+str(t0)+' y0 = '+str(y0))
##          #  ax.plot(time,solution_4(time,y0))
#    ax.set_aspect('equal')
#    ax.set_ylim(-2.5,2.5)

    plt.title(f"Equation u_1 = {expr} \n")
    plt.tight_layout()
#    plt.legend()
    plt.savefig(f'fields/field_exercise_{index}.jpg',bbox_inches='tight',pad_inches=0.2)

    plt.show()


plot_field(expr_24,22)

#for index,expr in enumerate(expr_list):
#    plot_field(expr,index)
