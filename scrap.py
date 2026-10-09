import numpy as np 
import matplotlib.pyplot as plt

f = lambda t,a: a*np.cosh(t)
g = lambda t,a: a*np.sinh(t)
z = lambda f,g: -f**2 + g**2
t = np.linspace(-1,1)
a = np.linspace(-1,1)
T, A = np.meshgrid(t,a)
left = f(T,A)
right = g(T,A)
ax = plt.figure().add_subplot(projection='3d')

ax.plot_surface(left,right,z(left,right),cmap='viridis')
ax.contour3D(left,right,z(left,right),cmap='plasma')
#ax.plot_surface(f(T,A),g(T,A),T)
#ax.contour3D(f(T,A),g(T,A),A)
#ax.contour3D(f(T,A),g(T,A),T)
plt.show()

