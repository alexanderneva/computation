
import numpy as np 
import matplotlib.pyplot as plt

G = 6.6743e-11


def f(t,s_1,s_2,s_1p=np.zeros(2),s_2p=np.zeros(2),m_1=1.,m_2=1.):
    y_1 = s_1
    y_2 = s_2
    y_3 = s_1p
    y_4 = s_2p
    #x_0 = np.vstack([y_1,y_2,y_3,y_4])
    r_12 = np.linalg.norm(s_1-s_2)
    y_1_p = y_1 - t*(y_3 @ s_1-s_2) / r_12
    y_2_p = y_2 + t*(y_4 @ s_2-s_1) / r_12
    y_3_p = -0.5*t*(s_1-s_2) * G *  m_2   / r_12**2
    y_4_p = 0.5*t*(s_2 -s_1) * G * m_1 / r_12**2
    #v_1_p = np.vstack([y_1_p,y_2_p,y_3_p,y_4_p])
    #x_1 = np.array([y_1,y_2,y_3])+t*v_1_p[0:3]+t**2*v_1_p[3:]
    return y_1_p,y_2_p,y_3_p,y_4_p

s_1 = np.random.normal(loc=(2,2))
s_2 = np.random.normal(loc=(-2,2))
s_1_i = s_1.copy()
s_2_i = s_2.copy()
print(f"s_1 {s_1}\n s_2 {s_2}")

total_step = 100
time = np.arange(1,total_step)

m_1 = 300e3
m_2 = 5e4
length = np.size(time)
print(length)
points = np.zeros(shape=(length+1,2,2))
pos = np.vstack([s_1_i,s_2_i])
points[0,...] += pos



#s_1,s_2,v_1,v_2 = f(h,s_1,s_2,s_1,s_2)
#print(s_1)
#print(s_2)
#print(v_1)
#print(v_2)
#
v_1=np.array([1,1])
v_2=np.array([-1,1])
#v_1 = np.zeros(2)
#v_2 = np.zeros(2)
for t in time:
    h = 0.25
    #s_1,s_2 = f(h,s_1,s_2,s_3)
    s_1,s_2,v_1,v_2 = f(h,s_1,s_2,v_1,v_2,m_1,m_2)
    pos = np.vstack([s_1,s_2])
    points[t,...] += pos
#
#
time = np.arange(0,total_step)
x_1 = points[time,0,...]
x_2 = points[time,1,...]


fig, ax = plt.subplots()
ax.plot(x_1[:,0],x_1[:,1],label=f'first mass {m_1}')
ax.plot(x_2[:,0],x_2[:,1],label=f'second mass {m_2}')
ax.scatter(s_1_i[0],s_1_i[1],label=f'first initial point',color='red')
ax.scatter(s_2_i[0],s_2_i[1],label=f'second initial point',color='red')
plt.legend()
plt.show()
