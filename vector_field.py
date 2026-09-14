import numpy as np
import matplotlib.pyplot as plt
from functools import partial

expr_0 = '2*y'
expr_1 = '-y**2'
expr_2 = 't*y'
expr_3 = '1- t**2 - y**2'
expr_4 = '1 + y**2'
expr_5 = 't**2+ y**2'


def f_1(t,y):
    return eval(expr_0)
def f_2(t,y):
    return eval(expr_1)

def f_3(t,y):
    return eval(expr_2)

def f_4(t,y):
    return eval(expr_3)

def f_5(t,y):
    return eval(expr_4)

def f_6(t,y):
    return eval(expr_5)

funcs = [f_1,f_2,f_3,f_4,f_5,f_6]
exprs = [expr_0,expr_1,expr_2,expr_3,expr_4,expr_5]


test = np.linspace(-10,10,25)
I, J = np.meshgrid(test,test)
step = 0.1
#fig, ax = plt.subplots(3,2)

for index,(func,expr) in enumerate(zip(funcs,exprs)):
    plt.figure()
    U = I + step
    V = step * func(I,J) + J
    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
    q = plt.quiver(I,J,U,V,scale=25)
    plt.quiverkey(q, X=0.3,Y=1.1,U=2,label='Length of 2',labelpos='E')
    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
    plt.title("Equation "+expr)
    plt.savefig(f'fields/field{index}.jpg')

#    plt.show()
        
