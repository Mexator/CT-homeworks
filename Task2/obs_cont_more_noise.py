from scipy.signal import place_poles
from random import randint
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import lqr

START=0
STOP=5
STEP=0.01
COUNT = int((STOP-START)/STEP)

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

C = np.asarray([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])

desired_poles = [-10, -20, -30, -40]
var = place_poles(A, B, desired_poles)
K = var.gain_matrix

L = lqr.get_L(A-B.dot(K), C)

dynamics_noise = np.random.normal(0,1,(COUNT,4))

def actual_sys(x, t, count=0):
    return (A-B.dot(K)).dot(x) + dynamics_noise[count]

def euler(f,y0,a=START,b=STOP,h=STEP,order=4):
    count = int((b-a)/h)
    ts=np.zeros(count)
    ys=np.zeros((count,order))
    t,y = a,y0
    ind = 0
    while t < b and ind < int((b-a)/h):
        ts[ind] = t
        ys[ind] = y
        t += h
        y += h * f(y,t, count=ind)
        ind += 1
    return (ts,ys)

output_noise = np.random.normal(0,1,(COUNT,2))

def estimated_sys(x_hat, t, count=0):
    x_hat_r = x_hat.reshape(4, 1)

    temp_space = [0, t]

    x = euler(actual_sys, initial, b=t, h=STEP)[1][-1]
    y = C.dot(x)
    y += output_noise[count]
    y = y.reshape(2, 1)

    y_hat = C.dot(x_hat)
    y_hat = y_hat.reshape(2, 1)

    return ((A-B.dot(K)).dot(x_hat).reshape((4,1)) + L.dot(y - y_hat)).reshape((4,))
 

initial = np.asarray([randint(0, 10) for _ in range(4)], dtype=np.float)
estimator_initial = np.asarray([0 for _ in range(4)], dtype=np.float64)
space = np.arange(start=0, stop=5, step=0.01)

sol = euler(actual_sys, initial)[1][:,:2]

estimation = euler(estimated_sys,estimator_initial)
err = estimation[1][:,:2] - sol

plt.subplot(3, 1, 1)
plt.title("actual system output")
plt.plot(space, sol)
plt.subplot(3, 1, 2)

plt.plot(estimation[0],estimation[1][:,:2])
plt.title("estimated output")
plt.subplot(3, 1, 3)
plt.title("output error")
plt.plot(space, err)
plt.savefig("est_cont_more_noise_out.pdf")
plt.show()
