# 스트라이크 게임  두 자리로 게임하면서 스트라이크는 있지만 볼은 없다.
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

case_all = []
case_ans = []
ti_as = []

for i in range(1,9+1):
    for j in range(1,9+1):
        case_all.append([i,j])
        if i == j :
            case_ans.append(1)
        else :
            case_ans.append(0)

print(case_all)        
        
for i in range(81):
    ti_a = []
    num1 = case_all[i][0]
    ti_a.append((num1-1)/8);
    num2 = case_all[i][0]
    ti_a.append((num2-1)/8);
    ti_as.append(ti_a)

for i in range(81):
    print(ti_as[i],case_ans[i])    


#
train_images = np.array(ti_as)
train_labels = np.array(case_ans)

print("train_images",train_images)
print("train_labels",train_labels)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)  

model = models.Sequential()
model.add(layers.Dense(1024, activation='relu', input_shape=(2,))) 
model.add(layers.Dense(1024, activation='relu'))   # 두 번 쓰는 방법인공지능이 100%가 안나오는 중..
model.add(layers.Dense(2, activation='softmax')) 


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=25) 

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)

for idx,r in enumerate(predicted_result) :
    print(idx,np.argmax(r))