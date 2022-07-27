# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

class AiLCP :
    def __init__(self):
        self.model = tf.keras.models.load_model('mnist_lcp.h5')
    
    def guess(self,train_images_a):
        train_images = np.array(train_images_a)
        predicted_result = self.model.predict(train_images)
        ai_answer = np.argmax(predicted_result[0])
        return ai_answer

if __name__ == '__main__' :
    lcp = AiLCP()
    ans = lcp.guess([[0.5]])
    print("ans",ans)
    

