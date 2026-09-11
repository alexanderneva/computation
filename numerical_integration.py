import math
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
#f = lambda x : math.exp(-x**2)
fr = lambda y : np.cos(np.pi*0.5*y**2)
frs = lambda z : np.sin(np.pi*0.5*z**2)
moment = lambda m,x : x**m * np.exp(-x)
gamma = lambda x,t : t**(x-1) * np.exp(-t)
gauss = lambda x : np.exp(-x**2)
test = lambda x : np.exp(np.cos(x))



def num_int(f,a=0.,b=1.,n=1000):
    sum = 0
    sum_lower = 0 
    sum_upper = 0

    h = (b-a) / n 
    for i in range(n+1):
        x = a + i*h
        sum = sum + f(x)
    sum_lower = sum*h
    sum_upper = sum_lower +h*(f(b)-f(a))
    epsilon = np.abs(sum_lower - sum_upper)
    return sum_lower, sum_upper,epsilon


def routine(f,a,b,epsilon):
    n= 100
    sum_lower,sum_upper,error = num_int(f,a,b,n)
    print(f"Epsilon {epsilon}")
    while error > epsilon:
        sum_lower,sum_upper,error = num_int(f,a,b,n)
        n+=100
        if n % 100 == 0:
            print("Tick")
    return np.mean([sum_lower,sum_upper]),n

#print(routine(fr,0,1,1e-3))



def adaptive_simpson(f,a,b,epsilon,level,level_max):
    level += 1
    h = b - a
    c = (a + b) / 2
    one_simpson = h*(f(a)+4*f(c)+f(b)) / 6
    d = (a + c) / 2
    e = (c + b) / 2
    two_simpson = h*(f(a) + 4*f(d) + 2*f(c) + 4*f(e) + f(b)) / 12
    if level >= level_max:
        simpson_result = two_simpson
    else:
        if np.abs(two_simpson - one_simpson) < 15*epsilon:
            simpson_result = two_simpson + (two_simpson - one_simpson) / 15
        else:
            left_simpson = adaptive_simpson(f,a,c,epsilon / 2, level, level_max)
            right_simpson = adaptive_simpson(f,c,b,epsilon / 2, level, level_max)
            simpson_result = left_simpson + right_simpson
    return simpson_result


f = lambda x : np.cos(2*x) / np.exp(x)
#result = adaptive_simpson(f,0,5/4*np.pi,0.5e-3,1,3)
book_result, _ = integrate.quad(f,0,5/4*np.pi)
#print(result,book_result)

levels = np.arange(1,20)
re = np.zeros_like(levels)
print("Book result", book_result)

for level in levels:
    result = adaptive_simpson(f,0,5/4*np.pi,0.5e-15,level,np.max(levels))
    print(result)
    re[level-1] = np.log(np.abs(book_result - result) / book_result)

print(re)
plt.plot(re)
plt.title("Logarithmic RE")
plt.show()

#sum_lower,sum_upper,epsilon = num_int(gauss,0,1,1000)
#print(sum_lower,sum_upper)
#print(f"Epsilon {epsilon}")
#
#
#x = np.linspace(-1,1,100)
#
#print(num_int(lambda x : gauss(x)))
#
#az = num_int(test,0,np.pi,1000)
#print(f"Test for int e^cos(x) {np.mean(az)}")
#
#print(integrate.quad(test,0,np.pi))
#
#fig, fig_1 = plt.subplots(3)
#fig_1[0].plot(x,fr(x))
#fig_1[0].set_title("Fresnel cosine integrand")
#fig_1[1].plot(x,frs(x))
#fig_1[1].set_title("Fresnel sine integrand")
#fig_1[2].plot(x,moment(5,x))
#
#plt.show()
#print(0.5*math.sqrt(math.pi)*math.erf(1))
#print(integrate.quad(f,0,1))

