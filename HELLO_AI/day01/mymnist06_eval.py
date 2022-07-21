# 문제 test안의 o폴더와 x 폴더에 구글과 나의 ai값이 같은지 판단 후 맞는 폴더에 넣기
# .png양식은 저장이름 구글답_내ai답_0.png  , 저장이름 구글답_내ai답_1.png
import cv2
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

g_train_labels = train_labels
print(train_labels[0])


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,))) # input이 784자리
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels, epochs=5, batch_size=128) 
# epochs이 늘어날수록(계산을 많이함) accuracy(정확도)가 늘어난다.
# batch_size ex) 6만건 데이터중에 샘플링을 128번 하는 것  숫자가 낮을수록 학습속도가 느리다?
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("test_acc",test_acc)

predicted_result = model.predict(train_images)

for idx, img in enumerate(train_images) :
    google_label =  g_train_labels[idx]
    ai_label = np.argmax(predicted_result[idx])
    if google_label == ai_label:
        cv2.imwrite('test/o/'+str(g_train_labels[idx])+'_'+str(ai_label)+'_'+str(idx)+'.jpg',train_images[idx])
    else :
        cv2.imwrite('test/x/'+str(g_train_labels[idx])+'_'+str(ai_label)+'_'+str(idx)+'.jpg',train_images[idx])





        
        
        
        
        