import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2

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

