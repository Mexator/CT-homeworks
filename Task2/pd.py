import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint

# constants
step = 0.001
final_time = 1
mu = 63 
k = 15

# function to obtain reference plot from function 
def get_ref(count,step,func):
    res = []
    for i in np.arange(0,count,step):
        res.append(func(i))
    return [np.linspace(0,count,int(count/step)),res]

# desired functions
def f_des(t):
    return 1
def f_dot_des(t):
    return 0

ref_x = get_ref(final_time,step,f_des)[1]
ref_x_dot = get_ref(final_time,step,f_dot_des)[1]

kp = 2000
kd = 13

def controlled_system(x,t):
    error = f_des(t) - x[0]
    error_dot = f_dot_des(t) - x[1]
    u = kp*error + kd*error_dot
    return np.array([x[1],(u - mu*x[1] - k*x[0])]) 

f=plt.figure()

times = np.linspace(0,final_time,int(final_time/step))
solution = odeint(controlled_system,[0,0],times)

plt.subplot(2, 1, 1)
plt.plot(times, solution[:,0], label = 'obtained x')
plt.plot(times, ref_x, label = 'ref_x')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(times, solution[:,1], label = 'obtained x_dot')
plt.plot(times, ref_x_dot, label = 'ref_x_dot')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend()
# plt.show()

f.savefig("ReportSources/2b_2.pdf", bbox_inches='tight')