from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np



train_images = np.load("train_data.npy")
train_labels = np.load("train_label.npy")

train_labels_c = to_categorical(train_labels,num_classes=11)
print("train_labels_c",train_labels_c)
 
model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(2,)))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(11, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=30)

model.save("2.h5")

predict_result = model.predict(train_images)
print("predict_result",predict_result)

for r in predict_result :
    ai_answer = np.argmax(r)
    print(ai_answer,end=",")


