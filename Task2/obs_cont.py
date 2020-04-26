from scipy.signal import place_poles
from random import randint
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

import lqr

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


def actual_sys(x, t):
    return (A-B.dot(K)).dot(x)


def estimated_sys(x_hat, t):
    x_hat_r = x_hat.reshape(4, 1)

    temp_space = [0, t]

    x = odeint(actual_sys, initial, temp_space)[-1, :]
    x = x.reshape(4, 1)

    return (actual_sys(x,t).reshape((4,1)) + L.dot(C.dot(x-x_hat_r))).reshape((4,))


initial = [randint(0, 10) for _ in range(4)]
estimator_initial = np.array([0 for _ in range(4)])
space = np.arange(start=0, stop=5, step=0.01)

sol = odeint(actual_sys, initial, space)[:,0:2]
estimation = odeint(estimated_sys, estimator_initial, space)[:,0:2]
err = estimation - sol

plt.subplot(3, 1, 1)
plt.title("actual system output")
plt.plot(space, sol)
plt.subplot(3, 1, 2)
plt.plot(space, estimation)
plt.title("estimated output")
plt.subplot(3, 1, 3)
plt.title("output error")
plt.plot(space, err)
plt.savefig("est_cont_out.pdf")
plt.show()
