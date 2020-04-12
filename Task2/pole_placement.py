from scipy import signal
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import random as rand

A = np.array([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 23.66, 0, 0],
    [0, 37.6, 0, 0]
])

B = np.array([
    [0], [0], [0.294], [0.294]
])

P = [-1+0j, -3-0j, -2-1j, -2+1j]

sys = signal.place_poles(A,B,P)
K = sys.gain_matrix
print('K = ',K,'\n','Poles = ',sys.computed_poles)

def dx(x,t):
    return A.dot(x) - B.dot(K.dot(x))
def unstabilized(x,t):
    return A.dot(x)

def random():
    return rand.randint(-100,100)
def random_vec(len=4):
    return np.array([random() for i in range(0,len)])

# Co=np.array([
#     [0, 0, 1, 0],
#     [0,0,0,1],
#     [1.076, -39.016, 2.2956, -10.2956],
#     [1.076, -25.076, 2.2956, -10.2956]
# ])


fig = plt.figure()
time = np.arange(0,10,0.01)
init = random_vec()
sol = odeint(dx,init,time)
plt.plot(time,sol)
plt.legend(["x","theta","x_dot","theta_dot"])
fig.text(.5, 0.025, f"System response with initial vector {init}", ha='center')
plt.show()
fig.savefig("Task2/Fig4.pdf",bbox_inches='tight')