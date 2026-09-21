import numpy as np 
import matplotlib.pyplot as plt

G = 6.6743e-11


def f(t,s_1,s_2,s_3,s_1p=0,s_2p=0,s_3p=0):
    y_1 = s_1
    y_2 = s_2
    y_3 = s_3
    y_4 = s_1p
    y_5 = s_2p
    y_6 = s_3p
    x_0 = np.array([y_1,y_2,y_3])
    r_12 = np.linalg.norm(s_1-s_2)
    r_23 = np.linalg.norm(s_2-s_3)
    r_13 = np.linalg.norm(s_1-s_3)
    y_1_p = y_4
    y_2_p = y_5
    y_3_p = y_6
    y_4_p = -G*(m_2*r_13**2 + m_3*r_12**2) / (r_12*r_13)**2
    y_5_p = -G*(m_1*r_23**2 + m_3*r_12**2) / (r_12*r_23)**2
    y_6_p = -G*(m_3*r_12**2 + m_1*r_23**2) / (r_23*r_12)**2
    v_1_p = np.array([y_1_p,y_2_p,y_3_p,y_4_p,y_5_p,y_6_p])
    #x_1 = np.array([y_1,y_2,y_3])+t*v_1_p[0:3]+t**2*v_1_p[3:]
    x_1 = x_0 + t*v_1_p[0:3] + 0.5*t**2*v_1_p[3:]


    return x_1

s_1 = np.random.normal(loc=(2,2,2),size=(1,3))
s_2 = np.random.normal(loc=(2,-2,-2),size=(1,3))
s_3 = np.random.normal(loc=(-2,2,2),size=(1,3))
s_1_i = s_1.copy()
s_2_i = s_2.copy()
s_3_i = s_3.copy()
print(f"s_1 {s_1}\n s_2 {s_2} \n s_3 {s_3}")

total_step = 100
time = np.arange(1,total_step)

m_1 = 300e3
m_2 = 5e4
m_3 = 7e5
length = np.size(time)
print(length)
points = np.zeros(shape=(length+1,3,3))
pos = np.vstack([s_1_i,s_2_i,s_3_i])
points[0,...] += pos


for t in time:
    h = 0.25
    s_1,s_2,s_3 = f(h,s_1,s_2,s_3,1,1,1)
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
ax.scatter(s_1_i[:,0],s_1_i[:,1],s_1_i[:,2],label=f'first initial point',color='red')
ax.scatter(s_2_i[:,0],s_2_i[:,1],s_2_i[:,2],label=f'second initial point',color='red')
ax.scatter(s_3_i[:,0],s_3_i[:,1],s_3_i[:,2],label=f'third initial point',color='red')
plt.legend()
plt.show()
