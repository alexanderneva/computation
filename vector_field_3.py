import numpy as np
import matplotlib.pyplot as plt
import itertools
from expression_generator import make_expression_list


def evaluator(t,x,y,expr_1,expr_2):
    return eval(expr_1),eval(expr_2)

n_expr = 7
n_op = 3
exprs = make_expression_list(n_expr,n_op)
exprs_pairs = itertools.combinations(exprs,2)


test = np.linspace(-10,10,25)
I, J = np.meshgrid(test,test)

for index,exprs in enumerate(exprs_pairs):
    fig, ax = plt.subplots()
    U,V = evaluator(I,I,J,exprs[0],exprs[1])
    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
    length = np.sqrt(U**2 + V**2)
    q = ax.quiver(I,J,U / length,V / length,scale=25,angles='xy')
    ax.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='S')
    ax.set_aspect('equal')
    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
    plt.title(f"Equation u_1 = {exprs[0]} \n u_2 = {exprs[1]} ")
    plt.tight_layout()
    plt.savefig(f'fields/field_3_{index}.jpg',dpi=200)

    plt.show()
        
