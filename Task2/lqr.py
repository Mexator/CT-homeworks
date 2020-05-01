from control import lqr
import numpy as np

def get_L(A,C):
    A_s = A.T 
    C_s = C.T

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
    return L
