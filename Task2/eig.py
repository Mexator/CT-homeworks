import numpy as np

A = np.asarray([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0.7796, 0, 0],
    [0, 30.256, 0, 0]
])

print(np.linalg.eig(A)[0])