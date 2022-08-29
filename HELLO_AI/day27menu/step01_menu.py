
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


train_images_a = [
        [1,0,0,0,0,  0,1,0,0,0,  0,0,1,0,0],
        [0,1,0,0,0,  0,0,1,0,0,  0,0,0,1,0],
        [0,0,1,0,0,  0,0,0,1,0,  0,0,0,0,1],
        [0,0,0,1,0,  0,0,0,0,1,  1,0,0,0,0],
        [0,0,0,0,1,  1,0,0,0,0,  0,1,0,0,0]
        
        
]
train_labels_a = [ 
    3,4,0,1,2
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(15,))) # input이 4 자리
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(5, activation='softmax')) #output 2자리


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=20) #epochs = 학습 횟수

model.save("menu.h5")

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)










