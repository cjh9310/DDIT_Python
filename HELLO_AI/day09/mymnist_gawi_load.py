# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

train_images_a = [[1,0,0]] # 0.5 => 2,   1 => 0, 0 => 0.5
train_images = np.array(train_images_a)

model = tf.keras.models.load_model('mnist_gawi.h5')

predicted_result = model.predict(train_images)

ai_answer = np.argmax(predicted_result)  
print("ai_answer",ai_answer)

