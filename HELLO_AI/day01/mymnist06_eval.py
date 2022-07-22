# 문제 test안의 o폴더와 x 폴더에 구글과 나의 ai값이 같은지 판단 후 맞는 폴더에 넣기
# .png양식은 저장이름 구글답_내ai답_0.png  , 저장이름 구글답_내ai답_1.png
import cv2
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
 
# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_labels[0])

g_train_labels = train_labels
g_train_images = train_images
# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
 
# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
 
# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))
 
# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
 
# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)
# epochs이 늘어날수록(계산을 많이함) accuracy(정확도)가 늘어난다.
# batch_size ex) 6만건 데이터중에 샘플링을 128번 하는 것  숫자가 낮을수록 학습속도가 느리다?
predict_result = model.predict(train_images)

cntO = 0;
cntX = 0;

for i in range(60000):
    go_label = g_train_labels[i]
    ai_label = np.argmax(predict_result[i])
    if go_label == ai_label:
        # cv2.imwrite('test/o/' + str(go_label) + "_" + str(ai_label) + "_" + str(i) +'.png', g_train_images[i])
        cv2.imwrite('test/o/{}_{}_{}.png'.format(go_label,ai_label,i), g_train_images[i])
        
    else : 
        cv2.imwrite('test/x/' + str(go_label) + "_" + str(ai_label) + "_" + str(i) +'.png', g_train_images[i])



        
        
        
        
        