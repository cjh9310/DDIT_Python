# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

train_images_a = [ # 사용자가 내는 것
        [1,0],  # 1,0 홀
        [0,1]   # 0,1 짝
]
train_images = np.array(train_images_a)

print("train_images",train_images) 


model = tf.keras.models.load_model('mnist_holl.h5')

predicted_result = model.predict(train_images)

ai_answer = np.argmax(predicted_result)  # ai 대답 0=홀, 1=짝
print("ai_answer",ai_answer)

