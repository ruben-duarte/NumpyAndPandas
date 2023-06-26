import numpy as np
import matplotlib.pyplot as plt

#parameters
n = 1000000
t = np.logspace(np.log10(10),np.log10(500),n)

# f represents frequency, p represents phase, A represents amplitude, d represents damping and t represents time

A = [1,4,2.5,4.5]
d = [.004, .007, .002, .0015]
f = [2,1,4,2.5]

# generate xy values pairs

x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)

#plot ! fun stuff
plt.plot(x, y, 'k', linewidth=.1)
plt.axis('off')
plt.show()

#elementary components
#plt.plot(np.sin(t*f[0])*np.exp(-d[0]*t), linewidth=.5)
#plt.show()
