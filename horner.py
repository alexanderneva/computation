import numpy as np

def poly(a,x):
    p = a[-1]
    for i in reversed(range(0,np.size(a)-1)):
        p = a[i] + x*p

    return p


#a = np.array([0,1,1])
#x = 3

#print(poly(a,x))

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"Polynomial of index {i} {j} {k} Answer: {poly(np.array([i,j,k]),3)}")


