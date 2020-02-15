import scipy.integrate as sp_int
import numpy as np
import matplotlib.pyplot as plt
import convert

#derivative functions - default and in SS form
def derivativeDE(x,t):
    dx = x[1:].copy()
    dx = np.append(dx,convert.a.dot(x))
    return dx

def derivativeSS(x,t):
    dx=convert.A.dot(x)
    return dx

#initial conditions
initial = np.array([4,3])
#time samples
time = np.linspace(0, 10, 1000)
#solution and plots   
sol1 = sp_int.odeint(derivativeDE,initial,time)
sol2 = sp_int.odeint(derivativeSS,initial,time)
plt.subplot(1,2,1)
plt.plot(time, sol1)
plt.xlabel('time')
plt.ylabel('x(t)')

plt.subplot(1,2,2)
plt.plot(time, sol2)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

e,v=np.linalg.eig(convert.A)
print(e)