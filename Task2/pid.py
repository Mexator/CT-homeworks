import numpy as np
import matplotlib.pylab as plt


# time - time step,
# reference - reference trajectory, array
# feedback - output of plant, array
# returns correction signal
def PID_controller (time, step, reference, feedback,
    PGain=1,IGain=1,DGain=1):
    if time == 0:
        return 0
    error = reference[time] - feedback[time]

    reference_dot = (reference[time] - reference[time-1])/step
    feedback_dot = (feedback[time] - feedback[time-1])/step
    error_dot = reference_dot - feedback_dot
    
    reference_int = np.sum(reference[:time])*step
    feedback_int = np.sum(feedback[:time])*step
    error_int = reference_int - feedback_int
    
    return PGain*error + DGain * error_dot + IGain * error_int

def get_ref(count,step,func):
    res = []
    for i in np.arange(0,count,step):
        res.append(func(i))
    return [np.linspace(0,count,int(count/step)),res]

def f(x):
    return np.sin(x)+x
def g(x):
    return np.sin(x)
ref_arr = get_ref(100,0.1,f)[1]
feed_arr = get_ref(100,0.1,g)[1] 

# x=np.linspace(0,100,1000)
# plt.plot(get_ref(100,0.1)[1],get_ref(100,0.1)[0])
def get_contr(count, step,p,i,d):
    res=[]
    for iterator in range(0,int(count/step)):
        res.append(PID_controller(iterator,step,ref_arr,feed_arr,p,i,d))
    return [np.linspace(0,count,int(count/step)),res]

p = get_contr(100,0.1,1,0,0)
i = get_contr(100,0.1,0,1,0)
d = get_contr(100,0.1,0,0,1)
plt.plot(p[0],p[1])
# plt.plot(i[0],i[1])
plt.plot(d[0],d[1])
plt.show()