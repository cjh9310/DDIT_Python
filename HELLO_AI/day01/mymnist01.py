# mymnist 분석하기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("train_images", train_images.shape) # (60000, 28, 28)  28은 픽셀값
print("train_labels", train_labels.shape)

print("test_images",test_images.shape)
print("test_labels",test_labels.shape)

# train은 6만개의 숫자
# test는 1만개의 숫자를 보유중 
# 각각의 train과 test는 images와 labels의 같은 숫자를 가지고 있음 ex) 같은 배열의  images가 5모양이면 labels도 숫자 5가 뜸. 
print("train_labels[]", train_labels[0])

for row in train_images[0] :
    for data in row :
        print(data, end="\t")
    print()