import numpy as np
from numpy.polynomial import Chebyshev
import matplotlib.pyplot as plt
import scipy.stats as stat
from scipy.integrate import quad
from scipy.stats import gaussian_kde
from scipy.interpolate import CubicSpline


def multi_res(f,j,n):
    """Given a function f, dilate it by 2**j and translate it 2**(-j)*n direction"""
    return lambda x : np.sqrt(2**j)*f(2**j*x-2**(-j)*n)


expr = 'x**6'
def f(x):
    """Signal to analyze"""
    return eval(expr)

plt.plot(np.linspace(-1,1,100),f(np.linspace(-1,1,100)))
plt.title('Signal '+ expr)
plt.grid()
plt.savefig('mra/signal.jpg',dpi=150)
plt.show()


fig, ax = plt.subplots(3,3,figsize=(8,8))
for j,ax in enumerate(ax.flat):
    for n in range(-3,3):
        x = np.linspace(-2**(8-j),2**(8-j),100)
        y = multi_res(lambda x : stat.norm.pdf(x),j-3,n)
        l = np.linalg.norm(y(x))
        #ax.plot(x,y(x)+((-1)**n)*0.25*n,label=f'translate  {-n} ')
        ax.plot(x,y(x)/l+((-1)**n)*0.25*n,label=f'translate  {-n} ')
        ax.set_xlim(-2**(8-j),2**(8-j))
        ax.set_title(f"Scaling at level {j-4} and translates",fontsize=9)
        ax.tick_params('both',labelsize=5)
        ax.grid(True)
#        ax.legend()
plt.tight_layout()
plt.savefig('mra/example_basis.jpg',dpi=150)
plt.show()

fig, ax = plt.subplots(3,3,figsize=(8,8))
for j,ax in enumerate(ax.flat):
    for n in range(-3,3):
        x = np.linspace(-2**(8-j),2**(8-j),100)
        y = multi_res(lambda x : stat.norm.pdf(x),j-3,n)
        #noise = np.random.normal(x)
        #fs = f(x) + noise
        #z = np.convolve(fs,y(x),mode='same')
        z = lambda x : f(x)*y(x)
        l = np.linalg.norm(z(x))
        #ax.plot(x,y(x)+((-1)**n)*0.25*n,label=f'translate  {-n} ')
        ax.plot(x,z(x)/l+((-1)**n)*0.25*n,label=f'translate  {-n} ')
        ax.set_xlim(-2**(8-j),2**(8-j))
        ax.set_title(f"Product scaling at level {j-4} and translates",fontsize=9)
        ax.tick_params('both',labelsize=5)
        ax.grid(True)
#        ax.legend()
plt.tight_layout()
plt.savefig('mra/example_basis_product.jpg',dpi=150)
plt.show()


coefs = []
k=0
basis_funcs = []
for j in range(9):
    for n in range(-3,3):
        x = np.linspace(-2**(8-j),2**(8-j),100)
        y = multi_res(lambda x : stat.norm.pdf(x),j-3,n)
        basis_funcs.append(y)
        #noise = np.random.normal(x)
        fs = f(x)
        #z = np.convolve(fs,y(x),mode='same')
        z = lambda x : f(x)*y(x) 
        z, _ = quad(z,-2,2)
        point = k
        coefs.append(np.array([point,z]))
        k += 1

coefs = np.array(coefs)
#interp = np.polynomial.Chebyshev(coefs[:,1],domain=[-1,1])
points = coefs[:,0]
n = len(coefs)
normalized_points = 2*points / (n-1) - 1


phi = np.vstack([func(normalized_points) / np.linalg.norm(func(normalized_points)) for func in basis_funcs ])
construc = coefs[:,1]@phi


interp = CubicSpline(normalized_points,coefs[:,1])
interp_2 = Chebyshev(coefs[:,1])
interp_3 = gaussian_kde(coefs[:,1],bw_method='scott')
plt.scatter(normalized_points,coefs[:,1],label='Raw coef')
plt.plot(normalized_points,interp(normalized_points),label='Cubic Spline')
plt.plot(normalized_points,interp_2(normalized_points), label = 'Chebyshev')
plt.plot(normalized_points,interp_3(normalized_points), label = 'Gaussian KDE')
plt.tick_params('both',labelsize=5)
plt.grid(True)
plt.ylim(-1,15)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('mra/curve_fitting_coefs.jpg',dpi=150)
plt.show()

plt.step(normalized_points,coefs[:,1])
plt.fill_between(normalized_points,coefs[:,1],step='mid',alpha=0.3)
plt.title('Step plot of coefficients')
plt.savefig('mra/step_plot_fixed_interval.jpg',dpi=150)
plt.show()


plt.plot(normalized_points,construc,label='reconstructed curve')
plt.plot(normalized_points,f(normalized_points),label='original curve')
plt.title("Reconstruction integrating on [-2,2]")
plt.legend()
plt.grid(True)
plt.savefig('mra/reconstruction_fixed_interval.jpg',dpi=150)
plt.show()


### change interval of integration

coefs = []
k=0
basis_funcs = []
for j in range(9):
    for n in range(-3,3):
        x = np.linspace(-2**(8-j),2**(8-j),100)
        y = multi_res(lambda x : stat.norm.pdf(x),j-3,n)
        basis_funcs.append(y)
        #noise = np.random.normal(x)
        fs = f(x)
        #z = np.convolve(fs,y(x),mode='same')
        z = lambda x : f(x)*y(x) 
        a = -1+2**(-j)*n
        b = 1+2**(-j)*n
        z, _ = quad(z,a,b)
        point = k
        coefs.append(np.array([point,z]))
        k += 1

coefs = np.array(coefs)
#interp = np.polynomial.Chebyshev(coefs[:,1],domain=[-1,1])
points = coefs[:,0]
n = len(coefs)
normalized_points = 2*points / (n-1) - 1


phi = np.vstack([func(normalized_points) / np.linalg.norm(func(normalized_points)) for func in basis_funcs ])
construc = coefs[:,1]@phi
plt.step(normalized_points,coefs[:,1])
plt.fill_between(normalized_points,coefs[:,1],step='mid',alpha=0.3)
plt.title('Step plot of coefficients')
plt.savefig('mra/step_plot_centered_interval.jpg',dpi=150)
plt.show()


plt.plot(normalized_points,construc,label='reconstructed curve')
plt.plot(normalized_points,f(normalized_points),label='original curve')
plt.legend()
plt.grid(True)
plt.savefig('mra/reconstruction_centered_interval.jpg',dpi=150)
plt.show()



### integrate over -inf,inf

coefs = []
k=0
basis_funcs = []
for j in range(9):
    for n in range(-3,3):
        x = np.linspace(-2**(8-j),2**(8-j),100)
        y = multi_res(lambda x : stat.norm.pdf(x),j-3,n)
        basis_funcs.append(y)
        #noise = np.random.normal(x)
        fs = f(x)
        #z = np.convolve(fs,y(x),mode='same')
        z = lambda x : f(x)*y(x) 
        b = np.inf
        a = -b
        z, _ = quad(z,a,b)
        point = k
        coefs.append(np.array([point,z]))
        k += 1

coefs = np.array(coefs)
#interp = np.polynomial.Chebyshev(coefs[:,1],domain=[-1,1])
points = coefs[:,0]
n = len(coefs)
normalized_points = 2*points / (n-1) - 1


phi = np.vstack([func(normalized_points) / np.linalg.norm(func(normalized_points)) for func in basis_funcs ])
construc = coefs[:,1]@phi
plt.step(normalized_points,coefs[:,1])
plt.fill_between(normalized_points,coefs[:,1],step='mid',alpha=0.3)
plt.title('Step plot of coefficients')
plt.savefig('mra/step_plot_whole_line.jpg',dpi=150)
plt.show()


plt.plot(normalized_points,construc,label='reconstructed curve')
plt.plot(normalized_points,f(normalized_points),label='original curve')
plt.legend()
plt.grid(True)
plt.savefig('mra/reconstruction_whole_line.jpg',dpi=150)
plt.show()
