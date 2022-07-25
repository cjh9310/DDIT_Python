# 분석하기01 + train_images를  train 폴더에 넣기
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

# 파일은 가져오는지 확인하기 위해 프린트 해보기
print("train_images.shape",train_images.shape)  # (50000, 32, 32, 3) 50000갯수, 32크기, 32크기, 컬러 3
print("train_labels.shape",train_labels.shape)  # (50000, 1)
print("test_images.shape",test_images.shape)    # (10000, 32, 32, 3)
print("test_labels.shape",test_labels.shape)    # (10000, 1)

for idx, img in enumerate(train_images) :
    Label = train_labels[idx][0]
    print(Label)   # train_labels가 배열로 되어있어서 뒤에 [0]을 추가해줘야함
    cv2.imwrite(f'train/{Label}/{idx}'+str(idx)+'.jpg',img)  # img = train_images[idx]