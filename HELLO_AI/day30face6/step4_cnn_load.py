import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")
test_images = np.load("test_image.npy")
test_labels = np.load("test_label.npy")

print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)

model = tf.keras.models.load_model('face.h5')

predictions = model.predict(test_images)

for i in range(1062):
    print(i, np.argmax(predictions[i]))

