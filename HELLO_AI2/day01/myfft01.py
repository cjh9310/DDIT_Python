import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0, 3, 1 / 100)
signal = 0.01 * np.sin(2 * np.pi * t) + 0.01 * np.sin(6*np.pi*t) 
print(t)
print(signal)

# fft = np.fft.fft(signal) / len(signal)  
fft = np.fft.fft(signal)
fft_magnitude = abs(fft)


plt.subplot(2,1,1)
plt.plot(t,signal)
plt.grid()
 
plt.subplot(2,1,2)
plt.stem(fft_magnitude)
plt.ylim(0,2.5)
plt.grid()
plt.show()