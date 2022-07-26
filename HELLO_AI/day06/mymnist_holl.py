# 홀짝 인공지능 100% 승리  신경망에 input 2개 output 2개  및 저장
import numpy as np
from day06 import myqt05
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


# 인공지능에게 학습시킬 조건
train_images_a = [ # 사용자가 내는 것
        [1,0],  # 1,0 홀
        [0,1]   # 0,1 짝
]
train_labels_a = [
    0,1     # 컴퓨터 : 0 홀 1 짝  
]



train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels) 
print("train_labels_c",train_labels_c)   

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(2,))) 
model.add(layers.Dense(2, activation='softmax')) 


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=5) 
test_loss, test_acc = model.evaluate(train_images, train_labels_c)
print("test_acc: ", test_acc)

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)

model.save('mnist_holl.h5')