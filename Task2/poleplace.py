from scipy.signal import place_poles
import numpy as np
def get_L(A,C):
    A_s = A.T
    C_s = C.T
    desired_poles = [-10, -20, -30, -40]

    var = place_poles(A_s,C_s,desired_poles)
    L = var.gain_matrix.transpose()
    # print("L=",L)
    return L
