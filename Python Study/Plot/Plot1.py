import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,10,0.01)
y,y1,y2 = 10*np.sin(x*x),x*x/10,1/x

plt.plot(x,y, label = 'sin(x*x)')
plt.plot(x,y1,label = 'X²/10')
plt.plot(x,y2,label = '1/x')


plt.xlabel('X')
plt.ylabel('Y')


plt.ylim(-10)
plt.xlim(0)
plt.legend()
plt.show()