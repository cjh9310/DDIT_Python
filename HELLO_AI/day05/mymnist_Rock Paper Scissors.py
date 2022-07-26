# 가위바위보 가위 100  , 바위 010 , 보 001      / 비김 0, 이김 1, 짐 2
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


train_images_a = [
        [0,0], # 가위(100) 가위(100) / train_labels_a 0
        [0,0.5], # 가위(100) 바위(010) / train_labels_a 1
        [0,1], # 가위(100) 보(001) / train_labels_a 2
        
        [0.5,0], # 바위(010) 가위(100) / train_labels_a 2
        [0.5,0.5], # 바위(010) 바위(010) / train_labels_a 0
        [0.5,1], # 바위(010) 보(001) / train_labels_a 1
        
        [1,0], # 보(001) 가위(100) / train_labels_a 1
        [1,0.5], # 보(001) 바위(010) / train_labels_a 2
        [1,1]  # 보(001) 보(001) / train_labels_a 0
        
]
train_labels_a = [ #비김 0, 짐 1, 이김 2
    0,1,2,2,0,1,1,2,0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(2,))) # input이 4 자리
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(3, activation='softmax')) #output 2자리


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=20) #epochs = 학습 횟수

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)










