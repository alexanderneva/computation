import numpy as np
import matplotlib.pyplot as plt


def cfb(n,a,b):
    """
    General backward continued fraction
    """
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return (a + b / cfb(n-1,a,b))

def fb(n):
    """
    Backward Continued fraction for (1+phi) / 2
    """
    if n==1 or n ==0:
        return 1
    else:
        return (1 + 1 / fb(n-1))


def ff(n,step):
    """
    Forward Continued fraction for (1+phi) / 2
    """
    if n==step:
        return 1
    else:
        return (1 + 1 / ff(n+1,step))

def fibb(n):
    """Backward fibonacci"""
    if n==0 or n==1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

def fibf(n,step):
    """Forward fibonacci"""
    if n == step:
        return 1
    elif n <= 0:
        return 1
    else:
        return 1 + fibf(n+1,step)



def test():

    #plt.plot(points)
    #plt.title('Absolute error of forward and backward fibonacci ratio')
    #plt.savefig('iterative_results/forward_backward.jpg',dpi=200)
    """Tests"""
    N_step = 15
    N_params = 100
    points = np.zeros([N_params,N_params])
    params = np.arange(1,N_params)
    for i in params:
        for j in params:
            points[i,j] += cfb(N_step,i,j)

    plt.figure(figsize=(15,10))        
    plt.plot(points[1:,1:].flatten())
    plt.title(f'{N_step} Step Backward Continued fraction over first {N_params} natural numbers')
    plt.savefig('iterative_results/cf_over_natural_grid.jpg',dpi=200)
    plt.close()


    endpoints = [0,1]
    N_endpoints = 100
    interval = np.linspace(endpoints[0],endpoints[1],N_endpoints)
    points = np.zeros([interval.size,4])
    for j,i in enumerate(interval):
        points[j,0] += cfb(N_step,i,1)
        points[j,1] += cfb(N_step,1,i)
        points[j,2] += cfb(N_step,1,i**2)
        points[j,3] += cfb(N_step,i**2,1)

    plt.figure(figsize=(15,10))        
    plt.plot(interval,points[:,0],label=r'$f(n)=a + 1/f(n-1)$')
    plt.plot(interval,points[:,1],label=r'$f(n)=1 + a/f(n-1)$')
    plt.plot(interval,points[:,2],label=r'$f(n)=1 + a^2/f(n-1)$')
    plt.plot(interval,points[:,3],label=r'$f(n)=a^2 + 1/f(n-1)$')
    plt.legend()
    plt.title(f'{N_step} Step Backward Continued fraction over interval {endpoints}')
    plt.savefig('iterative_results/cf_over_real_grid.jpg',dpi=200)
    return 0 

points = np.zeros(30)
for i in range(30):
    points[i] += np.abs(fb(i+2)/fb(i+1) - (1+np.sqrt(5))/2) / np.abs(fb(i+1)/fb(i) - (1+np.sqrt(5))/2)

plt.plot(points)
plt.grid()
plt.show()

def g(x):
    return (3*x+2) / (x + 2)

def iterate(g,x_0,step):
    """
    Backward iterate a function step times at point x_0
    """
    if step == 0:
        return g(x_0)
    else:
        return iterate(g,g(x_0),step-1)

def g_1(x):
    return (3*x+4)/(x+1)

def g_2(x):
    return np.sqrt(2*x+4)

for i in range(0,10):
#    print(iterate(g_2,i,6))
#    print(iterate(g_1,i,6))
    print(fibb(i+1)/fibb(i))
