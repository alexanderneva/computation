import numpy as np
import matplotlib.pyplot as plt

#def f(t,x,y):
#    return x - y + t*(2-t*(1+t)), x + y + t**2 * (-4+t)
#
#
#def taylor_system(f,x,y,a,b,n):
#    t = a
#    h = (b - a) / n
#    points = np.zeros([3,n])
#    for i in range(n):  
#        points[0,i] = t
#        points[1,i] = x
#        points[2,i] = y
#        x_p,y_p = f(t,x,y)
#        x_pp = x_p - y_p + 2 -t*(2+3*t)
#        y_pp = x_p + y_p + t*(-8+3*t)
#        x_ppp = x_pp - y_pp - 2 - 6*t
#        y_ppp = x_pp + y_pp -8 + 6*t
#        x_pppp = x_ppp - y_ppp - 6
#        y_pppp = x_ppp + y_ppp + 6
#        x = x + h*(x_p + 0.5*h*(x_pp + (1/3)*h*(x_ppp + 0.25 * h * x_pppp)))
#        y = y + h*(y_p + 0.5*h*(y_pp + (1/3)*h*(y_ppp + 0.25 * h * y_pppp)))
#        t = t + h
#
#    return points
#
#
#def taylor_system_2(f,x,y,a,b,n):
#    t = a
#    h = (b - a) / n
#    points = np.zeros([2,4])
#    xs = np.array([x,y])
#    pos = xs 
#    for i in range(n):
#        points[0,0] = x - y + t*(2-t*(1+t))
#        points[1,0] = x + y + t**2*(t-4)
#        points[0,1] = points[0,0] + points[1,0] + 2 - t*(2+3*t)
#        points[1,1] = points[0,0] + points[1,0] + t*(-8+3*t)
#        points[0,2] = points[0,1] - points[1,1] - 2 - 6*t
#        points[1,2] = points[0,1] + points[1,1] - 8 + 6*t
#        points[0,3] = points[0,2] - points[1,2] - 6
#        points[1,3] = points[0,2] + points[1,2] + 6
#        for j in range(2):
#            xs[j] = x + h*(points[j,0] + 0.5*h*(points[j,1] + (1/3)*h*(points[j,2]+0.25*h*points[j,3])))
#        t += h
##        print(f"{i,t,xs}")
#
#    return xs
#
##print(taylor_system_2(f,2,-1,0,1,100))
#
#
#
#t,x,y = taylor_system(f,1,0.2,1,3,200)
##print(t)
##print(x)
#
#ax = plt.figure().add_subplot(projection='3d')
#ax.scatter(0.01*t,x,y,zdir='t')
#ax.set_xlabel('t')
#ax.set_ylabel('x')
#ax.set_zlabel('y')
#plt.savefig("odes/taylor_system.jpg")
#plt.show()
#plt.close()
#
#
s0=0.999
gamma = 0.1
lamb = 0.59
r0 = s0*lamb / gamma
#
def sir(t,x,y,z):
    return -lamb*x*y, lamb*x*y - gamma*y,gamma*y
#
#
#
#def taylor_system_3(f,s,i,r,a,b,n):
#    """Second Order Approximation for 3-dim ode"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#        s_p,i_p,r_p = f(t,s,i,r)
#        s_pp = -lamb*(i_p*s + s_p*i)
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        r_pp = gamma*i_p
#
#   #     x_ppp = x_pp - y_pp - 2 - 6*t
#   #     y_ppp = x_pp + y_pp -8 + 6*t
#   #     x_pppp = x_ppp - y_ppp - 6
#   #     y_pppp = x_ppp + y_ppp + 6
#
#        s += h*(s_p + 0.5*h*(s_pp)) 
#        i +=  h*(i_p + 0.5*h*(i_pp)) 
#        r +=  h*(r_p + 0.5*h*(r_pp)) 
#        t += h
#
#    return points
#
#t,s,i,r = taylor_system_3(sir,s0,0.001,0,0,100,200)
#
#plt.plot(0.5*t,s, label='susceptible')
#plt.plot(0.5*t,i, label='infected')
#plt.plot(0.5*t,r, label='recovered')
#plt.xlabel('Time')
#plt.ylabel('Percentage')
#plt.title(f"Second order approx lambda {lamb} gamma {gamma}")
#plt.legend()
#plt.savefig('odes/sir_system_2.jpg')
#plt.show()
#plt.close()
#
#
#def taylor_system_4(f,s,i,r,a,b,n):
#    """Third Order Approximation for 3-dim ode"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#        s_p,i_p,r_p = f(t,s,i,r)
#        s_pp = -lamb*(i_p*s + s_p*i)
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        r_pp = gamma*i_p
#        s_ppp = -lamb*(i_pp*s + 2*s_p*i_p + i*s_pp)
#        i_ppp = s_ppp - gamma*i_pp
#        r_ppp = gamma*i_pp
#
#
#        s +=  h*(s_p + 0.5*h*(s_pp + h*(1/3)*s_ppp))
#        i +=  h*(i_p + 0.5*h*(i_pp + h*(1/3)*(i_ppp))) 
#        r +=  h*(r_p + 0.5*h*(r_pp + h*(1/3)*(r_ppp)))
#        t += h
#
#    return points
#
#
#t,s,i,r = taylor_system_4(sir,s0,0.001,0,0,100,200)
#
#plt.plot(0.5*t,s, label='susceptible')
#plt.plot(0.5*t,i, label='infected')
#plt.plot(0.5*t,r, label='recovered')
#plt.xlabel('Time')
#plt.ylabel('Percentage')
#plt.title(f"Third order approx lambda {lamb} gamma {gamma}")
#plt.legend()
#plt.savefig('odes/sir_system_3.jpg')
#plt.show()
#plt.close()
##
##
#def taylor_system_5(f,s,i,r,a,b,n):
#    """Fourth Order Approximation for 3-dim ode"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#        s_p,i_p,r_p = f(t,s,i,r)
#        s_pp = -lamb*(i_p*s + s_p*i)
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        r_pp = gamma*i_p
#        s_ppp = -lamb*(i_pp*s + 2*s_p*i_p + i*s_pp)
#        i_ppp = s_ppp - gamma*i_pp
#        r_ppp = gamma*i_pp
#        s_pppp = -lamb*(i_ppp*s + 3*s_p*i_pp + 3*i_p*s_pp)
#        i_pppp = s_pppp - gamma*i_ppp
#        r_pppp = gamma*i_ppp
#
#   #     x_ppp = x_pp - y_pp - 2 - 6*t
#   #     y_ppp = x_pp + y_pp -8 + 6*t
#   #     x_pppp = x_ppp - y_ppp - 6
#   #     y_pppp = x_ppp + y_ppp + 6
#
#        s += h*(s_p + 0.5*h*(s_pp + h*(1/3)*(s_ppp + h*0.25*s_pppp)))
#        i +=  h*(i_p + 0.5*h*(i_pp + h*(1/3)*(i_ppp+ h*0.25*i_pppp))) 
#        r +=  h*(r_p + 0.5*h*(r_pp + h*(1/3)*(r_ppp+ h*0.25*r_pppp)))
#        t += h
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#
#    return points
#
#
#t,s,i,r = taylor_system_5(sir,s0,0.001,0,0,100,200)
#
#plt.plot(0.5*t,s, label='susceptible')
#plt.plot(0.5*t,i, label='infected')
#plt.plot(0.5*t,r, label='recovered')
#plt.xlabel('Time')
#plt.ylabel('Percentage')
#plt.title(f"Fourth order approx lambda {lamb} gamma {gamma}")
#plt.legend()
#plt.savefig('odes/sir_system_4.jpg')
#plt.show()
#plt.close()
#
# 
## adding a recovered back into susceptible population at rate delta
#
delta = 0.1
def sir_f(t,x,y,z,delta,lamb,gamma):
    return -lamb*x*y+delta*x*z, lamb*x*y - gamma*y,gamma*y-delta*x*z
#
#def taylor_system_6(f,delta,gamma,lamb,s,i,r,a,b,n):
#    """Second Order Approximation for 3-dim ode with feedback"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#        s_p,i_p,r_p = f(t,s,i,r,delta,lamb,gamma)
#        s_pp = -lamb*(i_p*s + s_p*i) + delta*(r_p*s+r*s_p)
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        r_pp = gamma*i_p - delta*(r_p*s + r*s_p)
#        t += h
#
#        s += h*(s_p + 0.5*s_pp)
#        i += h*(i_p + 0.5*i_pp)
#        r += h*(r_p + 0.5*r_pp)
#
#
#
#
#    return points
#
#
#deltas = np.linspace(0.25,0.75,3)
#gammas = np.linspace(0.25,0.75,3)
#lambdas = np.linspace(0.25,0.75,3)
#
#for delta in deltas:
#    for gamma in gammas:
#        for lamb in lambdas:
#            t,s,i,r = taylor_system_6(sir_f,delta,gamma,lamb,0.9,0.1,0,0,100,200)
#            plt.plot(0.5*t,s, label='susceptible')
#            plt.plot(0.5*t,i, label='infected')
#            plt.plot(0.5*t,r, label='recovered')
#            plt.xlabel('Time')
#            plt.ylabel('Percentage')
#            plt.title(f"Second order approx lambda {lamb} gamma {gamma} delta {delta}")
#            plt.legend()
#            plt.savefig(f'odes/sir_system_{delta}_{gamma}_{lamb}.jpg')
#            plt.show()
#            plt.close()
#
def rk_system(f,s,i,r,a,b,n):
    t = a
    h = (b - a) / n
    points = np.zeros([4,n])
    for k in range(n):
        points[0,k] = t
        points[1,k] = s
        points[2,k] = i
        points[3,k] = r
        K1 = f(t,s,i,r)
        K2 = f(t+0.5*h,s+0.5*h*K1[0],i+0.5*h*K1[1],r+0.5*h*K1[2])
        K3 = f(t+0.5*h,s+0.5*h*K2[0],i+0.5*h*K2[1],r+0.5*h*K2[2])
        K4 = f(t+h, s + h*K3[0], i + h*K3[1], r + h*K3[2])
        t += h
        s += h / 6 *(K1[0]+2*K2[0]+2*K3[0]+K4[0])
        i += h / 6 *(K1[1]+2*K2[1]+2*K3[1]+K4[1])
        r += h / 6 *(K1[2]+2*K2[2]+2*K3[2]+K4[2])
    return points

t,s,i,r = rk_system(sir,0.9,0.1,0,0,100,200)

plt.plot(0.5*t,s, label='susceptible')
plt.plot(0.5*t,i, label='infected')
plt.plot(0.5*t,r, label='recovered')
plt.xlabel('Time')
plt.ylabel('Percentage')
plt.title(f"RK4 approx lambda {lamb} gamma {gamma}")
plt.legend()
#plt.savefig('odes/sir_system_rk.jpg')
plt.show()
plt.close()
#
#### competition system
##def f_competition(t,x,y,a,b,m,n):
##    return a*x - b*x*y,m*y-n*x*y
##
##def taylor_competition_2(f,a,b,m,n,x,y,t0,t1,n_step):
##    """Second order approximation of competition model"""
##    t = t0
##    h = (t1 - t0) / n_step
##    points = np.zeros([3,n_step])
##    for k in range(n_step):
##        points[0,k] += t
##        points[1,k] += x
##        points[2,k] += y
##        x_p,y_p= f(t,x,y,a,b,m,n)
##        x_pp = a*x_p - b*(x_p*y+x*y_p)
##        y_pp = m*y_p - n*(x_p*y+x*y_p)
##        t += h
##        x += h*(x_p+ 0.5*h*x_pp)
##        y += h*(y_p+ 0.5*h*y_pp)
##    
##    return points
##
##    
##a_s = np.arange(0.1,0.3,0.1)
##b_s = np.arange(0.1,0.3,0.1)
##m_s = np.arange(0.1,0.3,0.1)
##n_s = np.arange(0.1,0.3,0.1)
##
##for a in a_s:
##    for b in b_s:
##        for m in m_s:
##            for n in n_s:
##
##                t,x,y=taylor_competition_2(f_competition,a,b,m,n,1,1,0,20,100)
##                plt.plot(20*t/100,x, label='x')
##                plt.plot(20*t/100,y, label='y')
##                #plt.ylim(-10,10)
##                #plt.xlim(-1,1)
##                plt.xlabel('t')
##                plt.ylabel('y')
##                plt.title(f"Competition 2nd-order a {a} b {b} \n m {m} n{n}")
##                plt.legend()
##                plt.savefig(f'odes/competition_system_{a}{b}{m}{n}.jpg')
##                plt.close()
#
#def sir_g(t,x,y,z,delta,lamb,gamma):
#    """sir without delta*sr, just loss of immunity delta*r"""
#    return -lamb*x*y+delta*z, lamb*x*y - gamma*y,gamma*y-delta*z
#
#
#def taylor_system_7(f,delta,gamma,lamb,s,i,r,a,b,n):
#    """Second Order Approximation for 3-dim ode with feedback without interaction"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#        s_p,i_p,r_p = f(t,s,i,r,delta,lamb,gamma)
#        s_pp = -lamb*(i_p*s + s_p*i) + delta*r_p
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        r_pp = gamma*i_p - delta*r_p
#        t += h
#        s += h*(s_p + 0.5*s_pp)
#        i += h*(i_p + 0.5*i_pp)
#        r += h*(r_p + 0.5*r_pp)
#
#
#
#    return points
#
#
#deltas = np.linspace(0.25,0.75,3)
#gammas = np.linspace(0.25,0.75,3)
#lambdas = np.linspace(0.25,0.75,3)
#
#for delta in deltas:
#    for gamma in gammas:
#        for lamb in lambdas:
#            t,s,i,r = taylor_system_7(sir_g,delta,gamma,lamb,0.9,0.1,0,0,100,200)
#            plt.plot(0.5*t,s, label='susceptible')
#            plt.plot(0.5*t,i, label='infected')
#            plt.plot(0.5*t,r, label='recovered')
#            plt.xlabel('Time')
#            plt.ylabel('Percentage')
#            plt.title(f"Second order approx lambda {lamb} gamma {gamma} delta {delta}")
#            plt.legend()
#            plt.savefig(f'odes/sir_g_system_{delta}_{gamma}_{lamb}.jpg')
#            plt.show()
#            plt.close()



#def sir_r(t,x,y,z,delta,lamb,gamma):
#    """sir without delta*sr, just loss of immunity delta*r"""
#    return -lamb*x*y+delta*z, lamb*x*y - gamma*y
#
#
#def taylor_system_8(f,delta,gamma,lamb,s,i,r,a,b,n):
#    """Second Order Approximation for 3-dim ode with feedback without interaction, treating R in terms of S and I"""
#    t = a
#    h = (b - a) / n
#    points = np.zeros([4,n])
#    for k in range(n):
#        r = 1 - s - i
#        points[0,k] = t
#        points[1,k] = s
#        points[2,k] = i
#        points[3,k] = r
#        s_p,i_p = f(t,s,i,r,delta,lamb,gamma)
#        r_p = - s_p - i_p
#        s_pp = -lamb*(i_p*s + s_p*i) + delta*r_p
#        i_pp = lamb*(i_p*s + s_p*i) - gamma*i_p
#        t += h
#        s += h*(s_p + 0.5*s_pp)
#        i += h*(i_p + 0.5*i_pp)
#
#
#
#    return points
#
#
#t,s,i,r = taylor_system_8(sir_r,delta,gamma,lamb,0.9,0.1,0,0,100,200)
#plt.plot(0.5*t,s, label='susceptible')
#plt.plot(0.5*t,i, label='infected')
#plt.plot(0.5*t,r, label='recovered')
#plt.xlabel('Time')
#plt.ylabel('Percentage')
#plt.title(f"Second order approx lambda {lamb} gamma {gamma} delta {delta}")
#plt.legend()
#plt.savefig(f'odes/sir_r_system_{delta}_{gamma}_{lamb}.jpg')
#plt.show()
#plt.close()


def sirs_b(t,s,i,r,b,d,K,delta,lamb,gamma):
    """sirs with birth rate b and death rate d and population capacity K"""
    n = s + i + r 
    s_p = b*n - n**2 / K - lamb*s-d*s + delta*r
    i_p = lamb*i*s - (gamma+d)*i
    r_p = gamma*i - d*r - delta*r
    return s_p, i_p, r_p



def taylor_system_9(f,s,i,r,b,d,K,delta,gamma,lamb,t0,t1,n):
    t = t0
    h = (t1 - t0) / n

    points = np.zeros([4,n])
    for k in range(n):
        points[0,k] = t
        points[1,k] = s
        points[2,k] = i
        points[3,k] = r
        s_p,i_p,r_p = sirs_b(t,s,i,r,b,d,K,delta,lamb,gamma)
        n = s + i + r
        n_p = s_p + i_p + r_p
        s_pp = n*n_p - 2*n*n_p / K - (lamb -d)*s_p + delta*r_p
        i_pp = lamb*(i_p*s + s_p*i) - (gamma+d)*i_p
        r_pp = gamma*i_p - (d+delta)*r_p
        t += h
        s += h*(s_p + 0.5*s_pp)
        i += h*(i_p + 0.5*i_pp)
        r += h*(r_p + 0.5*i_pp)
    return points



deltas = np.linspace(0.25,0.75,3)
gammas = np.linspace(0.25,0.75,3)
lambdas = np.linspace(0.25,0.75,3)
bs = np.linspace(0,1,4)
#K = 1.5
#for b in bs:
#    d = 1-b
#    for delta in deltas:
#        for gamma in gammas:
#            for lamb in lambdas:
#                t,s,i,r = taylor_system_9(sirs_b,0.9,0.1,0,b,d,K,delta,gamma,lamb,0,30,200)
#                plt.plot(0.15*t,s, label='susceptible')
#                plt.plot(0.15*t,i, label='infected')
#                plt.plot(0.15*t,r, label='recovered')
#                plt.xlabel('Time')
#                plt.ylabel('Percentage')
#                plt.title(f"Second order approx \n Logistic Growth lambda {lamb} gamma {gamma} delta {delta} \n birth rate {np.round(b,2)} and death rate {np.round(d,2)} capacity K {K}")
#                plt.legend()
#                plt.savefig(f'odes/sirs_b_system_{delta}_{gamma}_{lamb}.jpg')
#                plt.tight_layout()
#                plt.show()
#                plt.close()
#
#b,d,K,delta,gamma,lamb,0,30,200)


#from rk import rk_system
#
#
def sir_v(lamb,gamma,t,x):
    """Vectorized sir with coefficients lambda and gamma"""
    s = x[0]
    i = x[1]
    return np.array([-lamb*s*i, lamb*s*i - gamma*i,gamma*i])
#
def sirs_bv(b,d,K,delta,lamb,gamma,t,x):
    """vectorized sirs with birth rate b and death rate d and population capacity K"""
    n = np.sum(x)
    s = x[0]
    i = x[1]
    r = x[2]
    s_p = b*n - n**2 / K - lamb*s-d*s + delta*r
    i_p = lamb*i*s - (gamma+d)*i
    r_p = gamma*i - d*r - delta*r
    return np.array([s_p, i_p, r_p])
#
#
#points,t = rk_system(lambda t,x : sir_v(0.9,0.1,t,x),np.array([0.9,0.1,0]),0,100,100)
#
#s = points[:,0]
#i = points[:,1]
#r = points[:,2]
#
#plt.plot(0.5*t,s, label='susceptible')
#plt.plot(0.5*t,i, label='infected')
#plt.plot(0.5*t,r, label='recovered')
#plt.xlabel('Time')
#plt.ylabel('Percentage')
#plt.title(f"RK4 approx lambda {lamb} gamma {gamma}")
#plt.legend()
##plt.savefig('odes/sir_system_rk.jpg')
#plt.show()
#plt.close()
#
#K = 1.5
#for b in bs:
#    d = 1-b
#    for delta in deltas:
#        for gamma in gammas:
#            for lamb in lambdas:
#                points,t = rk_system(lambda t,x :sirs_bv(b,d,K,delta,lamb,gamma,t,x),np.array([0.9,0.1,0]),0.,10.,100)
##                t = np.linspace(0,10,100)
#                s = points[:,0]
#                i = points[:,1]
#                r = points[:,2]
#                plt.plot(t,s, label='susceptible')
#                plt.plot(t,i, label='infected')
#                plt.plot(t,r, label='recovered')
#                plt.xlabel('Time')
#                plt.ylabel('Percentage')
#                plt.title(f"RK4 approx \n Logistic Growth lambda {lamb} gamma {gamma} delta {delta} \n birth rate {np.round(b,2)} and death rate {np.round(d,2)} capacity K {K}")
#                plt.legend()
##                plt.savefig(f'odes/sirs_bvrk4_system_{delta}_{gamma}_{lamb}.jpg')
##                plt.tight_layout()
#                plt.show()
#                plt.close()


def s_alpha(alpha,lamb,gamma,s,i,r):
    """S compartment with age transfer alpha and infection transfer lambda
    s (3,)     : s[0] first age group s[1] second age group
    alpha (n,) : transfer rate from s_1 to s_2
    lamb (n+1,): infection rate for s_1 and s_2"""

    s_1 = s[0]
    s_2 = s[1]
    s_3 = s[2]
    s_1_p = -(alpha[0]+lamb[0])*s_1
    s_2_p =  alpha[0]*s_1-alpha[1]*s_2 #-lamb[1]*s_2
    s_3_p = alpha[1]*s_2 - lamb[2]*s_3 
#    s_p = np.array([s_1_p,s_2_p,s_3_p])
    i_1 = i[0]
    i_2 = i[1]
    i_3 = i[2]
    i_1_p = lamb[0]*s_1 - gamma[0]*i_1 -alpha[0]*i_1
    i_2_p = lamb[1]*s_2 - gamma[1]*i_2 + alpha[0]*i_1 - alpha[1]*i_2
    i_3_p = lamb[2]*s_3 - gamma[2]*i_3 + alpha[1]*i_2
    r_1 = r[0]
    r_2 = r[1]
    r_3 = r[2]
    r_1_p = gamma[0]*i_1 - alpha[0]*i_1
    r_2_p = gamma[1]*i_2 + alpha[0]*i_1 - alpha[1]*r_2
    r_3_p = gamma[2]*i_3 + alpha[1]*r_2 - alpha[2]*r_3
    state = np.array([s_1_p,s_2_p,s_3_p,i_1_p,i_2_p,i_3_p,r_1_p,r_2_p,r_3_p])
    return state




def taylor_system_10(f,initial,alpha,lamb,gamma,t0,t1,n):
    """Naive 2 S compartment connection. Forward 2nd order"""
    t = t0
    h = (t1 - t0) / n
    points = np.zeros([10,n])

    s = initial[:,0]
    i = initial[:,1]
    r = initial[:,2]

    for k in range(n):
        points[0,k] = t
        points[1,k] = s[0]
        points[2,k] = s[1]
        points[3,k] = s[2]
        points[4,k] = i[0]
        points[5,k] = i[1]
        points[6,k] = i[2]
        points[7,k] = r[0]
        points[8,k] = r[1]
        points[9,k] = r[2]
        s_1_p,s_2_p,s_3_p,i_1_p,i_2_p,i_3_p,r_1_p,r_2_p,r_3_p = f(alpha,lamb,gamma,s,i,r)
        s_1_pp = -alpha[0]*s_1_p - lamb[0]*s_1_p
        s_2_pp = alpha[0]*s_1_p - lamb[1]*s_2_p - alpha[1]*s_2_p
        s_3_pp = alpha[1]*s_2_p - lamb[2]*s_3_p
        t += h
        s[0] += h*(s_1_p + 0.5*s_1_pp)
        s[1] += h*(s_2_p + 0.5*s_2_pp)
        s[2] += h*(s_3_p + 0.5*s_3_pp)
        i[0] += h*(i_1_p)
        i[1] += h*(i_2_p)
        i[2] += h*(i_3_p)
        r[0] += h*r_1_p
        r[1] += h*r_2_p
        r[2] += h*r_3_p
    return points


alpha = 0.5*np.ones(3)
lamb = np.array([0.1,0.3,0.7])
gamma = np.array([0.8,0.8,0.2])
initial_s = np.array([0.1,0.4,0.5])
initial_i = np.array([0.03,0.03,0.03])
initial_r = np.zeros(3)
initial = np.column_stack([initial_s,initial_i,initial_r])
points = taylor_system_10(s_alpha,initial,alpha,lamb,gamma,0,15,100)
t = points[0,:]
s_1 = points[1,:]
s_2 = points[2,:]
s_3 = points[3,:]
i_1 = points[4,:]
i_2 = points[5,:]
i_3 = points[6,:]
r_1 = points[7,:]
r_2 = points[8,:]
r_3 = points[9,:]

plt.plot(t,s_1, label='population 1')
plt.plot(t,s_2, label='population 2')
plt.plot(t,s_3, label='population 3')
plt.plot(t,i_1, label='infected population 1')
plt.plot(t,i_2, label='infected population 2')
plt.plot(t,i_3, label='infected population 3')
plt.plot(t,r_1, label='recovered population 3')
plt.plot(t,r_2, label='recovered population 3')
plt.plot(t,r_3, label='recovered population 3')
plt.xlabel('Time')
plt.ylabel('Percentage')
plt.title(f"Second order approx \n Three age compartments alpha = {alpha} \n lambda = {lamb}\n gamma = {gamma}")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig(f'odes/sir_alpha_system.jpg',dpi=200)
plt.show()
plt.close()
