# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np

class HerKY :
    def __init__(self):
        self.model = tf.keras.models.load_model('mnist_holl.h5')
    
    def guess(self,train_images_a): #맞추다.
        train_images = np.array(train_images_a)
        predicted_result = self.model.predict(train_images)
        ai_answer = np.argmax(predicted_result)
        return ai_answer

if __name__ == '__main__' :
    hky = HerKY()
    ans = hky.guess([[1,0]])
    print("ans",ans)
    

