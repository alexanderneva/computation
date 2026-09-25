import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.differentiate import jacobian

expr_0 = '2*y'
expr_1 = '-y**2'
expr_2 = 't*y'
expr_3 = '1- t**2 - y**2'
expr_4 = '1 + y**2'
expr_5 = 't**2+ y**2'
expr_6 = 't-y'
expr_7 = '-t-y'

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

def f_7(t,y):
    return eval(expr_6)
def f_8(t,y):
    return eval(expr_7)
def f_9(t,x_bar):
    x = x_bar[0]
    y = x_bar[1]
    return eval(expr_7),eval(expr_6)

funcs = [f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8]
exprs = [expr_0,expr_1,expr_2,expr_3,expr_4,expr_5,expr_6,expr_7]


#test = np.linspace(-10,10,25)
#I, J = np.meshgrid(test,test)
#step = 0.1
#fig, ax = plt.subplots(3,2)
#U,V = f_9(I,I,J)
#length = np.sqrt(U**2 + V**2)
#U /= length
#V /= length
#

#sol = solve_ivp(f_9,np.array([0,2]),np.array([1,-1]),vectorized=True)
#t = sol.t
#y = sol.y

#plt.figure()
#U,V = f_9(I,[J,J])
##q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
#length = np.sqrt(U**2 + V**2)
#q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
#plt.quiverkey(q, X=0.3,Y=1.1,U=2,label='Length of 2',labelpos='E')
#for points in np.array([[0.1,1.2],[-1.1,0.1],[-2,-11.2]]):
#    jac = jacobian(lambda x_bar : f_9(0,x_bar),points)
##    print(jac.df)
#    vals = np.linalg.eigvals(jac.df)
##    print("value", vals.astype(float))
#    sol = solve_ivp(f_9,np.array([0,5]),points)
#    sol_2 = solve_ivp(f_9,np.array([0,5]),vals.astype(float))
#    t = sol.t / np.linalg.norm(t)
#    y = sol.y / np.linalg.norm(y)
#    y_2 = sol_2.y 
#    y_2 /= np.linalg.norm(y_2)
#    plt.plot(y[0],y[1])
#    #plt.plot(y_2[0],y_2[1])
#plt.show()




#print(U)
#print(J)
#plt.figure()
#q = plt.quiver(I,J, U / length, V / length, scale=25, angles ='xy')
#plt.quiverkey(q, X=0.1,Y=1.1,U=1,label='Length of 1',labelpos='E')
#plt.title(f" Field of x = {expr_7} and \n y = {expr_4}")
#plt.savefig(f'fields/field{9}.jpg')
#plt.show()
#for index,(func,expr) in enumerate(zip(funcs,exprs)):
#    plt.figure()
#    U = np.ones_like(I)
#    V = func(I,J)
#    #q = ax[index].quiver(i,j,i+0.5,0.5*func(i,j)+j)
#    length = np.sqrt(U**2 + V**2)
#    q = plt.quiver(I,J,U / length,V / length,scale=25,angles='xy')
#    plt.quiverkey(q, X=0.3,Y=1.1,U=2,label='Length of 2',labelpos='E')
#    #ax[index].quiverkey(q, X=0.3,Y=0.3,U=1,label='Test',labelpos='E')
#    plt.title("Equation "+expr)
##    plt.savefig(f'fields/field{index}.jpg')
#
##    plt.show()


from ode_system import sirs_bv

deltas = np.linspace(0.25,0.75,3)
gammas = np.linspace(0.25,0.75,3)
lambdas = np.linspace(0.25,0.75,3)
bs = np.linspace(0,1,4)
b = bs[1]
d = 1 - b
delta = deltas[1]
lamb = lambdas[1]
gamma = gammas[1]
K = 1.5

test = np.linspace(0,1,25)
x = np.meshgrid(test,test,test)

points = sirs_bv(b,d,K,delta,lamb,gamma,test,x)
U = points[:,0]
V = points[:,1]
W = points[:,2]

sol = solve_ivp(lambda t,x : sirs_bv(b,d,K,delta,lamb,gamma,t,x),(0,1),np.array([0.9,0.1,0.]),t_eval=test)
t = sol.t
y = sol.y
#print(y.shape)
#plt.plot(t,y[0,:],label='susc')
#plt.plot(t,y[1,:],label='inf')
#plt.plot(t,y[2,:],label='rec')
#plt.legend()
#plt.tight_layout()
#plt.show()
#length = np.sqrt(U**2 + V**2 + W**2)
ax = plt.figure().add_subplot(projection='3d')
for b in bs:
    for delta in deltas:
        for gamma in gammas:
            for lamb in lambdas:
                d = 1 - b
                points = sirs_bv(b,d,K,delta,lamb,gamma,test,x)
                u = points[:,0]
                v = points[:,1]
                w = points[:,2]
                ax.quiver(test,test,test,u,v,w ,length=0.1,normalize=True)
                ax.set_aspect('equal')
ax.scatter(y[0,:],y[1,:],y[2,:])
ax.set_xlabel("s")
ax.set_ylabel("i")
ax.set_zlabel("r")
#ax.set_zlim([np.min(y[2,:]),np.max(y[2,:])])
plt.tight_layout()
plt.show()
#ax.quiverkey(q, X=0.3,Y=1.1,U=1,label='Length of 2',labelpos='E')
