import numpy as np
import matplotlib.pyplot as plt
import itertools
from expression_generator import make_expression_list
from scipy.differentiate import jacobian
from scipy.integrate import LSODA

def evaluator(t,x_bar,expr_1,expr_2):
    x = x_bar[0]
    y = x_bar[1]
    return eval(expr_1),eval(expr_2)

n_expr = 7
n_op = 3
exprs = make_expression_list(n_expr,n_op)
exprs_pairs = itertools.combinations(exprs,2)


test = np.linspace(-10,10,25)
I, J = np.meshgrid(test,test)


U, V = evaluator(np.column_stack([I,J,J]),exprs[0],exprs[1])
initial = np.array([[0,0],[1,0]])
print(initial.shape)
f = lambda t : lambda x_bar : evaluator(t,x_bar,exprs[0],exprs[1])
od = LSODA(f,0,initial[:,1],1)

#for index,exprs in enumerate(exprs_pairs):
#    plt.figure()
#    U,V = evaluator(I,I,J,exprs[0],exprs[1])
#    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
#    length = np.sqrt(U**2 + V**2)
#    q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
#    plt.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='S')
#    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
#    plt.title(f"Equation u_1 = {exprs[0]} \n u_2 = {exprs[1]} ")
#    plt.savefig(f'fields/field_4_{index}.jpg',dpi=200)
#
#    plt.show()
        
