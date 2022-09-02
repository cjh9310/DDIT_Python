import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2

img1 = cv2.imread('train_eng/1/0.png')
print("img1",img1.shape)
train_images = img1.reshape((1,480,640,3))
train_images = train_images/255.0

# train_images = np.load("train_image.npy")
# train_labels = np.load("train_label.npy")
#
# print(train_images.shape)


model = tf.keras.models.load_model('ganada.h5')

predictions = model.predict(train_images)

print(np.argmax(predictions[0]))

