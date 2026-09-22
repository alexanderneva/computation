import numpy as np 
import matplotlib.pyplot as plt

G = 6.6743e-11


def f(t,s_1,s_2,s_3,s_1p=np.zeros(3),s_2p=np.zeros(3),s_3p=np.zeros(3)):
    y_1 = s_1
    y_2 = s_2
    y_3 = s_3
    v_1 = s_1p
    v_2 = s_2p
    v_3 = s_3p
    x_0 = np.array([y_1,y_2,y_3])
    r_12 = s_1 - s_2
    r_12n = np.linalg.norm(r_12)
    r_23 = s_2 - s_3
    r_23n = np.linalg.norm(r_23)
    r_13 = s_1 - s_3
    r_13n = np.linalg.norm(s_1-s_3)
    v_1 += t*G*(m_2*r_13n**2 + m_3*r_12n**2) / (r_12n*r_13n)**2 * (r_12 + r_13)
    v_2 += t*G*(m_1*r_23n**2 + m_3*r_12n**2) / (r_12n*r_23n)**2 * (r_12 + r_23)
    v_3 += t*G*(m_3*r_12n**2 + m_1*r_23n**2) / (r_13n*r_12n)**2 * (r_23 + r_12)
    y_1_p = t*v_1
    y_2_p = t*v_2
    y_3_p = t*v_3


    return y_1_p,y_2_p,y_3_p,v_1,v_2,v_3

s_1 = np.random.normal(loc=(2,2,2))
s_2 = np.random.normal(loc=(2,-2,-2))
s_3 = np.random.normal(loc=(-2,2,2))
v_1 = np.zeros(3)
v_2 = np.zeros(3)
v_3 = np.zeros(3)
s_1_i = s_1.copy()
s_2_i = s_2.copy()
s_3_i = s_3.copy()
print(f"s_1 {s_1}\n s_2 {s_2} \n s_3 {s_3}")


m_1 = 3e5
m_2 = 5e5
m_3 = 7e5

total_step = 500
time = np.arange(1,total_step)
length = np.size(time)
print(length)
points = np.zeros(shape=(length+1,3,3))
pos = np.vstack([s_1_i,s_2_i,s_3_i])
points[0,...] += pos


for t in time:
    h = 0.0001 
    s_1,s_2,s_3,v_1,v_2,v_3 = f(h,s_1,s_2,s_3,v_1,v_2,v_3)
    pos = np.vstack([s_1,s_2,s_3])
    points[t,...] += pos


time = np.arange(0,total_step)
ax = plt.figure().add_subplot(projection='3d')
x_1 = points[time,0,...]
x_2 = points[time,1,...]
x_3 = points[time,2,...]

print(np.shape(x_1))
ax.plot(x_1[:,0],x_1[:,1],x_1[:,2],label=f'first mass {m_1}')
ax.plot(x_2[:,0],x_2[:,1],x_2[:,2],label=f'second mass {m_2}')
ax.plot(x_3[:,0],x_3[:,1],x_3[:,2],label=f'third mass {m_3}')
ax.scatter(s_1_i[0],s_1_i[1],s_1_i[2],label=f'first initial point',color='red')
ax.scatter(s_2_i[0],s_2_i[1],s_2_i[2],label=f'second initial point',color='red')
ax.scatter(s_3_i[0],s_3_i[1],s_3_i[2],label=f'third initial point',color='red')
ax.scatter(x_1[-1,0],x_1[-1,1],x_1[-1,2],label=f'first terminal point',color='purple')
ax.scatter(x_2[-1,0],x_2[-1,1],x_2[-1,2],label=f'second terminal point',color='purple')
ax.scatter(x_3[-1,0],x_3[-1,1],x_3[-1,2],label=f'third terminal point',color='purple')
plt.legend()
plt.show()
