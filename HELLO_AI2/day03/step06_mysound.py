import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("file.wav")
# y, sr = librosa.load("luck.wav")
t = np.arange(0, len(y))

print(sr)
print(y)

sr = np.ones((200))

plt.plot(t,y)
plt.grid()
plt.show()

