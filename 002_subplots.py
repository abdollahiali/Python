import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t0 = 0 # initial value for t
tf = 1 # final value for t 
N = 100 # number of points
t = np.linspace(t0, tf, N) # creates a numpy array starting with t0 up to tf containing N samples with equal distances

f1 = 1; # frequency in Hz
x1 = np.sin(2*PI*f1*t)

f2 = 2; # frequency in Hz
x2 = np.sin(2*PI*f2*t)

f3 = 4; # frequency in Hz
x3 = np.sin(2*PI*f3*t)

f4 = 8; # frequency in Hz
x4 = np.sin(2*PI*f4*t)

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(t, x1, 'g')
#plt.xlabel('t (sec)')
plt.ylabel('x1')
plt.title('Sine Wave (frequency: 1 Hz)')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(t, x2, 'b')
#plt.xlabel('t (sec)')
plt.ylabel('x2')
plt.title('Sine Wave (frequency: 2 Hz)')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(t, x3, 'm')
plt.xlabel('t (sec)')
plt.ylabel('x3')
plt.title('Sine Wave (frequency: 4 Hz)')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(t, x4, 'r')
plt.xlabel('t (sec)')
plt.ylabel('x4')
plt.title('Sine Wave (frequency: 8 Hz)')
plt.grid()

plt.show()
