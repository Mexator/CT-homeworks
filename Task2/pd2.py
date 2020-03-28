import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy.linalg as nl

A = np.array([[10,3],[5,-5]])

def f_int_des(t):
    return t

def f_des(t):
    return 1

def f_dot_des(t):
    return 0

mu = 63
k=15
K_p = 40
K_i = 100
K_d = 1
step = 0.001
final_time = 100

def controlled_system(x,t):
    error_int = f_int_des(t) - x[0]
    error = f_des(t) - x[1]
    error_dot = f_dot_des(t) - x[2]
    u = K_p * error + K_d * error_dot + K_i * error_int
    return np.array([x[1],x[2],u-mu*x[2]-k*x[1]-9.8])

init = np.array([0,0,0])
times = np.linspace(0,final_time,int(final_time/step))

def get_ref(count,step,func):
    res = []
    for i in np.arange(0,count,step):
        res.append(func(i))
    return [np.linspace(0,count,int(count/step)),res]

ref_x_int = get_ref(final_time,step,f_int_des)[1]
ref_x = get_ref(final_time,step,f_des)[1]
ref_x_dot = get_ref(final_time,step,f_dot_des)[1]

f=plt.figure()

sol = odeint(controlled_system,init,times)
plt.subplot(3, 1, 1)
plt.plot(times, sol[:,0], label = 'obtained x_integral')
plt.plot(times, ref_x_int, label = 'ref_x_integral')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(times, sol[:,1], label = 'obtained x')
plt.plot(times, ref_x, label = 'ref_x')
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(times, sol[:,2], label = 'obtained x_dot')
plt.plot(times, ref_x_dot, label = 'ref_x_dot')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend()

f.savefig("Test{}-{}-{}.pdf".format(K_p,K_i,K_d), bbox_inches='tight')