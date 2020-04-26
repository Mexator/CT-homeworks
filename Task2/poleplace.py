from scipy.signal import place_poles
import numpy as np
A_s = np.asarray([
    [0, 0, 0, 0],
    [0, 0, 0.7796, 30.256],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])
C_s = np.asarray([
    [1,0],
    [0,1],
    [0,0],
    [0,0]
])
desired_poles = [-10, -20, -30, -40]

var = place_poles(A_s,C_s,desired_poles)
L = var.gain_matrix.transpose()
# print("L=",L)
# print(L.shape)