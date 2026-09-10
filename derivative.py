import math

n = 30
h = 1
error_max = 0.
x = 0.5

for i in range(n):
    h = 0.5*h
    y = (math.sin(x+h)-math.sin(x))/h
    error = abs(math.cos(x)-y)
    print(error)
    if error > error_max:
        emax = error
        imax = i

print(imax,emax)

