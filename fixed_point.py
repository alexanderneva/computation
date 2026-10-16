import numpy as np
import matplotlib.pyplot as plt
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

plt.plot(points)
plt.title('Absolute error of forward and backward fibonacci ratio')
plt.savefig('iterative_results/forward_backward.jpg',dpi=200)
