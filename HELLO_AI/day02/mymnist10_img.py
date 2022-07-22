# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('mnist.h5')

img = Image.open("0_0_1.png").convert("L") #L(256단계 흑백이미지)로 변환
test_data = ((np.array(img) / 255) - 1) * -1

predicted_result = model.predict(test_data)
print("predicted_result",predicted_result)

