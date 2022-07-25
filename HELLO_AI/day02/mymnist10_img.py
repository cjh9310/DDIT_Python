# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

img = cv2.imread('0_0_1.png')
train_images = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
train_images = train_images.reshape((1,784))
print(train_images[:1].shape)    # [:1]이 없을때 (28, 28)     /  [:1]이 있으면 (1, 28)

model = tf.keras.models.load_model('mnist.h5')

predicted_result = model.predict(train_images)

ai_answer = np.argmax(predicted_result[0])
print("ai_answer",ai_answer)

