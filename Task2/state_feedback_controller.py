from scipy.signal import place_poles
from random import randint
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

A = np.asarray([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0.7796, 0, 0],
    [0, 30.256, 0, 0]
])

B = np.asarray([
    [0],
    [0], 
    [0.066],
    [0.066]
])

desired_poles = [-10, -20, -30, -40]

var = place_poles(A,B,desired_poles)
K = var.gain_matrix

u = 0
def system(x,t):
    x = x.reshape(4,1)
    return (A.dot(x) + B.dot(u)).reshape(4,)

def controlled(x,t):
    return A.dot(x) - B.dot(K.dot(x))

initial = [randint(0, 10) for _ in range(4)]
space = np.arange(start=0, stop=5, step=0.01)

sol = odeint(system, initial, space)[:, 0:2]
contr = odeint(controlled, initial, space)[:, 0:2]

plt.subplot(2,1,1)
plt.title("uncontrolled system")
plt.plot(space,sol)
plt.subplot(2,1,2)
plt.title("system with controller")
plt.plot(space,contr)
plt.show()
