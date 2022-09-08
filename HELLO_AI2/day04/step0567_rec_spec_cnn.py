import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
 
#------------------------------------------------------- step5
MIC_DEVICE_ID = 1
 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 16000     # 카카오 음성 인식에서 요구하는 RATE
# 이것을 라즈베리파이에서는 인식을 못하여 아래 16k 변환 소스 참고
SAMPLE_SIZE = 2  # FORMAT의 바이트 수
 
def record(record_seconds):
    p = pyaudio.PyAudio()
    stream = p.open(input_device_index=MIC_DEVICE_ID,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start to record the audio.")
    frames = []
 
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
 
    print("Recording is finished.")
 
    stream.stop_stream()
    stream.close()
    p.terminate()
 
    return frames
 
 
# 녹음 데이터를 WAV 파일로 저장하기
def save_wav(target, frames):
    wf = wave.open(target, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_SIZE)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
 
    if isinstance(target, str):
        wf.close()
 
if __name__ == '__main__':
    RECORD_SECONDS = 3
    frames = record(RECORD_SECONDS)
 
    WAVE_OUTPUT_FILENAME = "output.wav"
    save_wav(WAVE_OUTPUT_FILENAME, frames)
#--------------------------------------------------- step06


def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.03 :
            pass
        else:
            break
        idx_f+=1
    
    idx_f -=40
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.03 :
            pass
        else:
            break
        idx_l-=1
    idx_l +=40
    
    return arr_n[idx_f:idx_l]

y, sr = librosa.load("file.wav")
y_trim = cutMute(y)

# y, sr = librosa.load("luck.wav")
t = np.arange(0, len(y_trim))

print(sr)
print(y_trim)

plt.specgram(y_trim)
plt.savefig("output.png")
plt.title('Spectrogram Using matplotlib.pyplot.specgram() method')  
plt.show() 

#--------------------------------------------------- step07

labels = [ "이상권", "김유미", "박수현", "박성우", "최재혁", "양형주"]


img1 = cv2.imread('output.png')
print("img1",img1.shape)
train_images = img1.reshape((1,480,640,3))
train_images = train_images/255.0

# train_images = np.load("train_image.npy")
# train_labels = np.load("train_label.npy")
#
# print(train_images.shape)


model = tf.keras.models.load_model('myvoice.h5')

predictions = model.predict(train_images)
l_idx = np.argmax(predictions[0])
print(l_idx,labels[l_idx])