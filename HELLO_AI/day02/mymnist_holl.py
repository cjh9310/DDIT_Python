# 홀짝 구하기  신경망에 input 4개 output 2개 
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# 인공지능에게 학습시킬 조건
train_images_a = [
        [1,0,1,0], # com 1,0홀 mine 1,0 홀  / train_labels_a의 0   이김 
        [1,0,0,1], # com 1,0홀 mine 0,1 짝  / train_labels_a의 1   패배
        [0,1,1,0], # com 0,1홀 mine 1,0 짝  / train_labels_a의 1   패배
        [0,1,0,1], # com 1,0홀 mine 1,0 홀 /  train_labels_a의 0   이김
        # images(문제)에 labels(답)을 학습시킴 train_labels_a에서 0은 정답 1은 오답으로
]
train_labels_a = [
    0,1,1,0
]

train_images = np.array(train_images_a)
train_labels = np.array(train_labels_a)

train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)   # 0 => [1,0], 1 => [0,1]    ex) 3 => [0,0,0,1]

model = models.Sequential()
model.add(layers.Dense(10, activation='relu', input_shape=(4,))) # input이 4 자리
model.add(layers.Dense(2, activation='softmax')) #output 2자리


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels_c, epochs=50, batch_size=4) 

predicted_result = model.predict(train_images)
print("predicted_result",predicted_result)


# train_labels_c [
#  [1. 0.] 
#  [0. 1.]
#  [0. 1.]
#  [1. 0.]]
                                        #   [확률 확인은 콘솔에서 accuracy 뒤의 값을 확인하면 됨. ex) 1.0 = 100%
# model.fit을 실행할 때 (인공지능 학습o)   50%    [뭐지? 학습량이 부족해서 찍는거랑 확률이 비슷하게 나온듯]
# predicted_result [[0.5574316  0.4425684 ] [해결 : epochs(학습량)을 늘려서 100%로 만듬]
#  [0.45388338 0.54611665]
#  [0.67650324 0.3234967 ]
#  [0.4694637  0.53053635]]

# model.fit을 주석처리하고 실행할 때 (학습 x)  50%
# predicted_result [[0.35236692 0.647633  ] 
#  [0.4199449  0.58005506]
#  [0.43979105 0.560209  ]
#  [0.5585779  0.44142213]]


