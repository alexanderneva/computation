import numpy as np
import matplotlib.pyplot as plt

def moment_test(f,max_step):
    """Simple test for highest x term"""
    n = max_step

    t = np.arange(0,50)
    f_min = np.min(f(t))
    max_errors=np.zeros(n)
    for j in range(n):

        deg = j
        x = np.zeros(50)
        for i in range(1,50):
            x[i] += f(i)/i**j-1

        max_error = np.max(x)
        max_errors[j]+=max_error
        if max_error == np.min(max_errors[j-1]):
            deg = j-1

            print("Max error reached at step", deg)
            return deg

        #print(f"Max error {np.max(x)} Average Error {np.mean(x)}")
        print(f"Max errors {max_errors}")
        plt.plot(t, x)
        plt.title(f"Moment for exponent {j}")
        plt.show()

    return deg


def f(x):
    return x**9+1

print("Moment test ", moment_test(f,13))
