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
    if n==1:
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

N_step = 150
points=np.zeros(N_step)
for i in range(1,N_step):
    points[i] += np.abs(fb(i)-ff(i,N_step)) 

#plt.plot(points)
#plt.title('Absolute error of forward and backward fibonacci ratio')
#plt.savefig('iterative_results/forward_backward.jpg',dpi=200)
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
plt.plot(interval,points[:,0],label=r'f(n)=a + 1/f(n-1)')
plt.plot(interval,points[:,1],label=r'f(n)=1 + a/f(n-1)')
plt.plot(interval,points[:,2],label=r'$f(n)=1 + a^2/f(n-1)$')
plt.plot(interval,points[:,3],label=r'$f(n)=a^2 + 1/f(n-1)$')
plt.legend()
plt.title(f'{N_step} Step Backward Continued fraction over interval {endpoints}')
plt.savefig('iterative_results/cf_over_real_grid.jpg',dpi=200)
