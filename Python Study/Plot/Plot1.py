import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,10,0.1)
x2 = np.arange(-10, -0.1, 0.1)
x = x + x2

a=10
b=20
print(x)

y,y1,y2,y3 = 10*np.sin(x*x),x*x/10,1/x,b*np.sqrt(1-x*x/a*a)

plt.plot(x,y, label = 'sin(x*x)')
plt.plot(x,y1,label = 'X²/10')
plt.plot(x,y2,label = '1/x')
#plt.plot(x,y3,label = 'x²/a*a+y²/b*b=1')


plt.xlabel('X')
plt.ylabel('Y')
#plt.contour()


#plt.ylim(-10)
#plt.xlim(0)
plt.legend()
plt.show()