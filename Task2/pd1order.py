import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy.linalg as nl

# Proportional and derivative gain
K_p = 10
K_d = 1
# Final time of integration, and integration step
final_time = 1
step = 0.001
# Our matrices A, B and K
A = np.array([[10,3],[5,-5]])
B = np.array([[1],[1]])
K=np.array([K_p,K_d])
# Desired state x is 0 => stable
x_desired = np.asarray([0, 0])

last_t = 0
last_error = np.asarray([0, 0])

def differential(x,t):
    global last_t, last_error
    error = x_desired - x
    dt = max(t - last_t,1e-6)
    de = error - last_error
    error_dot = de / dt

    error_1  = np.array([error[0],error_dot[0]])
    error_2  = np.array([error[1],error_dot[1]])
    u = K.dot(error_1 + error_2)

    x = x.reshape((2,1))
    x_dot = A.dot(x) + B.dot(u)

    last_t = t
    last_error = error
    x_dot = x_dot.reshape((2,))
    return x_dot

init = np.array([5,3])
times = np.arange(step, 1, step)
f = plt.figure()
sol = odeint(differential,init,times)
plt.plot(times, sol)
plt.show()
f.savefig("ReportSources/2d.pdf", bbox_inches='tight')