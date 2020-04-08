import numpy as np
from numpy.linalg import eig

A = np.array(
    [[0,0,1,0],
    [0,0,0,1],
    [0, 23.6, 0, 0],
    [0, 37.6, 0, 0]])

print(eig(A)[0])