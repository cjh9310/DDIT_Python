# 구글이 준 labels, ai가 준 labels  ,idx를 이용하여 구글과 ai의 값이 같으면 o 다르면 x에 넣어라
import cv2
import tensorflow as tf
import numpy as np
from keras.utils import to_categorical

# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

g_train_labels = train_labels
g_test_images = test_images

# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0   # 기존에는 색상이 0~255까지 나오는데 이것을 0~1까지만 나오게 해줌

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련
model.fit(train_images, train_labels, epochs=5, batch_size=128)

# 7. 예측하기
predict_result = model.predict(test_images)


for idx,img in enumerate(g_test_images) : 
    go_label = test_labels[idx]
    ai_label = np.argmax(predict_result[idx])
    #print(go_label, ai_label)  콘솔로 비교 확인해보기 
    if go_label == ai_label:
        # cv2.imwrite('test/o/' + str(go_label) + "_" + str(ai_label) + "_" + str(i) +'.png', g_train_images[i])
        cv2.imwrite('test/o/{}_{}_{}.png'.format(go_label,ai_label,idx), img) #format 방식
        
    else : 
        cv2.imwrite(f'test/x/{go_label}_{ai_label}_{idx}.jpg',img) # f'' 방식

