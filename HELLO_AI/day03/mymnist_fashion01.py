# train_Labels에 들어있는 첫 숫자 기준으로 train폴더에 차례대로 넣어라  ex)0.png  애니멀레이터 사용해서  아마 6만개의 그림 출력한 것 처럼 하면 될듯
import cv2
import tensorflow as tf
import numpy as np
from keras import models
from keras import layers
from keras.utils import to_categorical

# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


for idx, i in enumerate(train_labels):
    label = train_labels[idx]
    print(f'train/{label}/{idx}.jpg')  #실행되는지 확인하는 것
    cv2.imwrite(f'train/{label}/{idx}.jpg', train_images[idx])  # 폴더에 가져온 이미지 삽입