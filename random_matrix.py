import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt

A = np.array([[1,2],[2,1]])
data = []
for i in range(100):
    b = np.random.normal(size=(2,2))
    data.append(np.linalg.matrix_norm(A@b))

plt.plot(data)
plt.savefig('data.jpg')

print(np.min(data))

