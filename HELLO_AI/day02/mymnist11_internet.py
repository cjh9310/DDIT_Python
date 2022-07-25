# ai 숫자 공부
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

img = cv2.imread('8.jpg')
resize_img = cv2.resize(img, (28, 28)) # 크기 맞추기
train_images = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY) # 회색으로 바꾸기
cv2.imshow('dst1',train_images)
train_images = 256 - train_images   # 반전시키기
cv2.imshow('dst2',train_images)

train_images = train_images.reshape((1,784))
train_images = train_images.astype('float32') / 255



print(train_images.shape)    

model = tf.keras.models.load_model('mnist.h5')  # 저장한 ai 불러오기

predicted_result = model.predict(train_images)

ai_answer = np.argmax(predicted_result[0])
print("ai_answer",ai_answer)

