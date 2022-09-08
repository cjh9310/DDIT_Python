import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers


labels = [
    "이상권",
    "김유미",
    "박수현",
    "박성우",
    "최재혁",
    "양형주"
  ]

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")

print("Train samples:", train_images.shape, train_labels.shape)


train_images = train_images/255.0


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(480, 640, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(6, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=4)
model.save("myvoice.h5")


predictions = model.predict(train_images)

for i in range(10):
    print(i,np.argmax(predictions[i]))






