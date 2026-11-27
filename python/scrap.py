import numpy as np 
import matplotlib.pyplot as plt

##f = lambda t,a: a*np.cosh(t)
##g = lambda t,a: a*np.sinh(t)
##z = lambda f,g: -f**2 + g**2
##t = np.linspace(-1,1)
##a = np.linspace(-1,1)
##T, A = np.meshgrid(t,a)
##left = f(T,A)
##right = g(T,A)
##ax = plt.figure().add_subplot(projection='3d')
##
##ax.plot_surface(left,right,z(left,right),cmap='viridis')
##ax.contour3D(left,right,z(left,right),cmap='plasma')
###ax.plot_surface(f(T,A),g(T,A),T)
###ax.contour3D(f(T,A),g(T,A),A)
###ax.contour3D(f(T,A),g(T,A),T)
##plt.show()
#
##alpha = 0.5 
##beta = 0.1
##N_0 = 1000
##nu = 1/8
##beta = nu
##f = lambda alpha,beta : N_0*np.exp(-alpha/beta)
###z = lambda t : nu/(1+(nu/(1-nu))*np.exp(-beta*t))
###z = lambda a,y : y*(a-y**2)
###z = lambda alpha,p,t : p - 1 / (alpha*t + 1/p)
###z = lambda c,x : np.sqrt((2*c + x**4)/x**2)-x
##z = lambda x,y : (x+3/2)**2+(y-1)**2-13/4
#t = np.linspace(-10,10)
#
##plt.plot(t,f(alpha,t))
##plt.plot(t,f(t,beta))
##for i in t:
##    plt.plot(t,z(i,t))
##ps = np.linspace(-5,5)
#cs = np.linspace(-13/4,13/4)
#thetas = np.linspace(0,2*np.pi)
#
#X, Y = np.meshgrid(cs,thetas)
#def circle(C,theta):
#    R = np.sqrt(13/4+C)
#    x = R*np.cos(theta) - 3/2
#    y = R*np.sin(theta) + 1 
#    return np.array([x,y])
#
#x,y = circle(X,Y)
##plt.plot(x,y)
##plt.show()
#
#
#z = lambda f,g: np.sqrt(f**2 + g**2)
#ax = plt.figure().add_subplot(projection='3d')
#ax.plot_surface(x,y,z(x,y))
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.show()
#
#
#a_x = lambda x : 0.5*(x**3+2*x)
#b_x = lambda x : 0.5*(3-x**2)
#u_x = lambda a,b : np.cbrt(np.sqrt((a**2/4)+(b**3)/27)-a)
#y_x = lambda u,b : (3*u -b)/u
#
#x= np.linspace(-2,2)
#u = u_x(a_x(x),b_x(x))
#y = y_x(u,b_x(x))
#plt.plot(y)
#plt.show()
#
#
#def curve(a,b,c,C,y):
#    x = np.sqrt(C + (b**2-a*c)/a**2 * y**2) - b/a * y
#    return x
#
#a = 1
#c = 0.1
#b = 2
#y= np.linspace(-4,15)
#cs = np.linspace(-1,1)
#for c in cs:
#    plt.plot(y,curve(a,b,c,1,y))
#plt.show()
#
#
#def sol_2(a,theta):
#    x = np.sqrt(a)*np.cos(theta)+np.sqrt(a/3)*np.sin(theta)
#    y = np.sqrt(a)*np.cos(theta)-np.sqrt(a/3)*np.sin(theta)
#    return x,y 
#
#                                                    
#
#theta = np.linspace(0,2*np.pi)
#aes = np.arange(1,10)
#
#for a in aes:
#    x,y=sol_2(a,theta)
#    plt.plot(x,y,label=f"a = {a}")
#plt.xlim(-10,10)
#plt.ylim(-10,10)
#plt.legend()
#plt.show()
#
#
#b_y = lambda y : y/3 - 1
#c_y = lambda y : -2/3 * y**2
#
#x_u = lambda b,u : u - b / (3*u)
#
#u_bc = lambda b,c : np.cbrt(np.sqrt(((c-2)**2)/4 + (b/3)**3)-(c/2 -1))
#
#ys = np.linspace(-5,5)
#b = b_y(ys)
#c = c_y(ys)
#u = u_bc(b,c)
#x_sol = x_u(b,u)
#plt.plot(ys,x_sol)
#plt.show()
#
#
#
#def curve_1(k,x,y):
#    z = (x-y/6)**3 + (1/3)*(1/36)*y**3 + k/2
#    return z
#
#x = np.linspace(0,1)
#y = np.linspace(0,1)
#k = np.linspace(-1,1)
#X,Y = np.meshgrid(x,y)
#ax = plt.figure().add_subplot(projection='3d')
#for k_ in k:
#    ax.plot_surface(X,Y,curve_1(X,Y,k_))
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_zlabel('z')
#plt.title(f"Plot for k = {k_}")
#plt.show()
#
#
#def curve_2(t,c):
#    x = 1/np.sqrt(c) * (-np.sinh(t) + np.cosh(t))
#    y = 1/np.sqrt(c) * (np.sinh(t) + np.cosh(t))
#    return x,y
#
#t = np.linspace(-2,2)
#cs = np.linspace(1,5)
#for c in cs:
#    x,y=curve_2(t,c)
#    plt.plot(x,y)
#plt.show()

#for c in cs:
#    if p > 0:
#        plt.plot(t,z(X,Y),color='cyan')
#    else:
#        plt.plot(t,z(X,Y),color='pink')
        
#plt.axhline(1/8,color='red')
#plt.axhline(z(20),color='orange')
#plt.show()

