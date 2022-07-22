# 가위바위보 가위 100  , 바위 010 , 보 001      / 비김 0, 이김 1, 짐 2
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


train_images_a = [
        [1,0,0,1,0,0], # 가위(100) 가위(100) / train_labels_a 0
        [1,0,0,0,1,0], # 가위(100) 바위(010) / train_labels_a 1
        [1,0,0,0,0,1], # 가위(100) 보(001) / train_labels_a 2
        
        [0,1,0,1,0,0], # 바위(010) 가위(100) / train_labels_a 2
        [0,1,0,0,1,0], # 바위(010) 바위(010) / train_labels_a 0
        [0,1,0,0,0,1], # 바위(010) 보(001) / train_labels_a 1
        
        [0,0,1,1,0,0], # 보(001) 가위(100) / train_labels_a 1
        [0,0,1,0,1,0], # 보(001) 바위(010) / train_labels_a 2
        [0,0,1,0,0,1]  # 보(001) 보(001) / train_labels_a 0
        
]
train_labels_a = [ #비김 0, 이김 1, 짐 2
    0,1,2,2,0,1,1,2,0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(10, activation='relu', input_shape=(6,))) # input이 4 자리
model.add(layers.Dense(3, activation='softmax')) #output 2자리


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=500, batch_size=6)  #epochs = 학습 횟수

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)

print(train_labels_a)

# argmax를 써서 predicted_result자리에 인공지능이 고른 가장 높은 확률값을 선택 및 찾음 
# 현재 인공지능은 100% 확률도 맞춤 => 그래서 train_labels_a 값과 동일함
for r in predicted_result :
    ai_answer = np.argmax(r)
    print(ai_answer,end=", ")
print()







