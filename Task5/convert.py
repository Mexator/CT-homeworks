import numpy as np
#n - degree of the polynomial 
n = 3
# a - array of coefficients: [ak ak-1 ... a0]
a = np.array([1,-1,-7,])  

# normalization
a = a[1:] / a[0]
a=-a
# for convenience    
a=np.flip(a)

# state matrix
A = np.zeros((n-1, n-1)) 
A[n-2 , 0:] = a
A[0:(n-2),1:] = np.eye(n-2)

print("Matrix A:")
print(A)
b=np.array([1])
#In this case we have only one input value - b_0
print("Matrix B:")
print(b)