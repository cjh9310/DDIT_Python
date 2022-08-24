# 분석하기
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import models, layers, datasets
import cv2

# 라벨 0번쨰는 airplane
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# 데이터 
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

print(train_images.shape)
print(train_images[0])

# 이미지 폴더에 업데이트하기 (100개만)

for idx, img in enumerate(train_images) :
    cv2.imwrite(f'train_image/{idx}'+str(idx)+'.png',train_images[idx])
    if idx > 100:
        break  