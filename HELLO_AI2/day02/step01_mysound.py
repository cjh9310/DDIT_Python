import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("최재혁가1.mp3")
# y, sr = librosa.load("luck.wav")
t = np.arange(0, len(y))

print(sr)
print(y)

sr = np.ones((200))

plt.plot(t,y)
plt.grid()
plt.show()

