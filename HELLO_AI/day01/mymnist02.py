# train_images안에 있는 이미지들 생성 (총 6만개)
import cv2
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# for idx, img in enumerate(train_images) :
#     cv2.imwrite('train/'+str(idx)+'.jpg',train_images[idx])


cv2.imwrite('test/x/'+str(1)+'.jpg',train_images[1])
