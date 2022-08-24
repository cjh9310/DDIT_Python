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



np.save("train_images",train_images)
np.save("train_labels",train_labels)
np.save("test_images",test_images)
np.save("test_labels",test_labels)
