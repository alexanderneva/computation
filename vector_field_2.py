import numpy as np
import matplotlib.pyplot as plt
import itertools

expr_0 = '2*y'
expr_1 = '-y**2'
expr_2 = 't*y'
expr_3 = '1- t**2 - y**2'
expr_4 = '1 + y**2'
expr_5 = 't**2+ y**2'
expr_6 = 't-y'
expr_7 = '-t-y'

#def f_1(t,y):
#    return eval(expr_0)
#
#def f_2(t,y):
#    return eval(expr_1)
#
#def f_3(t,y):
#    return eval(expr_2)
#
#def f_4(t,y):
#    return eval(expr_3)
#
#def f_5(t,y):
#    return eval(expr_4)
#
#def f_6(t,y):
#    return eval(expr_5)
#
#def f_7(t,y):
#    return eval(expr_6)
#def f_8(t,y):
#    return eval(expr_7)
#def f_9(t,x,y):
#    return eval(expr_7),eval(expr_4)

def evaluator(t,x,y,expr_1,expr_2):
    return eval(expr_1),eval(expr_2)

#funcs = [f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8]
exprs = [expr_0,expr_1,expr_2,expr_3,expr_4,expr_5,expr_6,expr_7]
exprs_pairs = itertools.combinations(exprs,2)


test = np.linspace(-10,10,25)
I, J = np.meshgrid(test,test)
#step = 0.1
#fig, ax = plt.subplots(3,2)
#U,V = f_9(I,I,J)
#length = np.sqrt(U**2 + V**2)
#print(U)
#print(J)
#plt.figure()
#q = plt.quiver(I,J, U / length, V / length, scale=25, angles ='xy')
#plt.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='E')
#plt.title(f" Field of x = {expr_7} and \n y = {expr_4}")
#plt.savefig(f'fields/field{9}.jpg')
#plt.show()
for index,exprs in enumerate(exprs_pairs):
    plt.figure()
    U,V = evaluator(I,I,J,exprs[0],exprs[1])
    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
    length = np.sqrt(U**2 + V**2)
    q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
    plt.quiverkey(q, X=0.3,Y=1.1,U=1,label='Length of 1',labelpos='E')
    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
    plt.title(f"Equation u_1 = {exprs[0]} \n u_2 = {exprs[1]} ")
    plt.savefig(f'fields/field_2_{index}.jpg')

    plt.show()
        
