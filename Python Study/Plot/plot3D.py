import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')


t = np.linspace(-4*np.pi, 4*np.pi,500)

z = np.linspace(-4,4,500)/4
r = z**3 + 1
x = r*np.sin(t)
y = r*np.cos(t)

ax.plot(x,y,z,label = 'sprial')
ax.legend()
plt.show()