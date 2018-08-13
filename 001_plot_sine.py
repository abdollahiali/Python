import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
x0 = 0 # initial value for x
xf = 2*PI # final value for x 
dx = 0.1 # delta x
x = np.arange(x0, xf, dx) # creates a numpy array starting with x0 up to xf with steps equal to dx
y = np.sin(x)

plt.figure()
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')
plt.grid()

# or another way
fig, ax = plt.subplots()
ax.plot(x, y, 'red')
ax.set(xlabel = 'x', ylabel = 'y', title = 'Sine Wave')
plt.grid()
fig.savefig('SineFig.jpg') # saves the figure


plt.show()
