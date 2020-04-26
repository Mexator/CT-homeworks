import numpy as np
from scipy.integrate import odeint
from random import randint
import matplotlib.pyplot as plt

import poleplace
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

# L = poleplace.get_L(A,C)
L = lqr.get_L(A, C)

u = 0


def system(x, t):
    x = x.reshape(4,1)
    return (A.dot(x) + B.dot(u)).reshape(4,)


def estimator(x_hat, t):
    x_hat_r = x_hat.reshape(4, 1)

    temp_space = [0, t]

    y = C.dot(odeint(system, initial, temp_space)[-1, :])
    y = y.reshape(2, 1)

    y_hat = C.dot(x_hat)
    y_hat = y_hat.reshape(2, 1)

    return (system(x_hat,t).reshape((4,1)) + L.dot(y - y_hat)).reshape((4,))


def error(error_v, t):
    return (A-L.dot(C)).dot(error_v)


initial = [randint(0, 10) for _ in range(4)]
estimator_initial = np.array([0 for _ in range(4)])

space = np.arange(start=0, stop=5, step=0.01)
sol = odeint(system, initial, space)[:, 0:2]

estimated = odeint(estimator, estimator_initial, space)[:, 0:2]
# err = odeint(error,initial-estimator_initial,space)[:,0:2]
err = sol-estimated

plt.subplot(3, 1, 1)
plt.title("actual system output")
plt.plot(space, sol)
plt.subplot(3, 1, 2)
plt.plot(space, estimated)
plt.title("estimated output")
plt.subplot(3, 1, 3)
plt.title("output error")
plt.plot(space, err)
plt.show()
