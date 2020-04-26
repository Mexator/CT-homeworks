from control import lqr, ctrb
import poleplace
import numpy as np

A_s=poleplace.A_s
C_s=poleplace.C_s


Q = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])
Q *= 100
R = np.array([
    [1, 0],
    [0, 1],
])
K,S,E = lqr(A_s,C_s,Q,R)

L = np.asarray(K.transpose())
# print(L)