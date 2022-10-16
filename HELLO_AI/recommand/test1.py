from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
import tensorflow as tf
from tensorflow import keras

# AI_1 - 업종, 연차, 학점 정보를 통한 인재 추천

# -------------------- Input Code --------------------
# 업종 코드
input1 = [
        "서비스업",         # 0        
        "제조·화학",        # 1
        "IT·웹·통신",       # 2
        "은행·금융업",      # 3
        "미디어·디자인",    # 4
        "교육업",           # 5
        "의료·제약·복지",   # 6
        "판매·유통",        # 7
        "건설업",           # 8
        "기관·협회"         # 9
        ]

# 연차범위 코드 (단위:년차)
input2 = [
        "0 ~ 3",            # 0        
        "4 ~ 7",            # 1
        "8 ~ 11",           # 2
        "12 ~ 15",          # 3
        "16 ~ 19",          # 4
        "20 ~ 23",          # 5
        "24 ~ 27" ,         # 6
        "28 ~ 31" ,         # 7
        "32 ~ 35" ,         # 8
        "36 ~ 40"           # 9
        ]

# 학점범위 코드 (단위:점)
input3 = [
        "고졸",             # 0        
        "0.0 ~ 1.0",        # 1
        "1.1 ~ 1.5",        # 2
        "1.6 ~ 2.0",        # 3
        "2.1 ~ 2.5",        # 4
        "2.6 ~ 3.0",        # 5
        "3.1 ~ 3.5",        # 6
        "3.6 ~ 4.0",        # 7
        "4.1 ~ 4.4",        # 8
        "4.5"               # 9
        ]
# ----------------------------------------------------
# -------------------- Output Code --------------------
# 학위 코드
output1 = [
        "고졸",             # 0            
        "초대졸",           # 1
        "학사",             # 2
        "석/박사"           # 3
        ]

# 학과계열 코드
output2 = [
        # 고졸
        "고교 인문계열",    # 0        
        "고교 실업계열",    # 1
        "고교 예체능계열",  # 2
        # 초대졸 이상
        "인문계열",         # 3
        "사회계열",         # 4
        "교육계열",         # 5
        "자연계열",         # 6
        "공학계열",         # 7
        "의약계열",         # 8
        "예체능계열"        # 9       
        ]

# 연령범위 코드 (단위:세)
output3 = [
        "19 ~ 25",         # 0
        "26 ~ 30",         # 1
        "31 ~ 35",         # 2
        "36 ~ 40",         # 3
        "41 ~ 45",         # 4
        "46 ~ 50",         # 5
        "51 ~ 55",         # 6
        "56 ~ 60",         # 7
        "61 ~ 65",         # 8
        "66 ~ 80"          # 9 - 시니어
        ]
# -----------------------------------------------------


train_images_a = [    
                    [4, 2, 7], [4, 1, 7], [4, 0, 6], [2, 3, 0], [2, 0, 0], [3, 0, 8], [3, 0, 7], [8, 3, 0], [1, 1, 5], [7, 1, 0],
                    [5, 3, 6], [3, 1, 8], [9, 1, 6], [6, 5, 8], [7, 3, 4], [0, 4, 0], [2, 7, 5], [1, 2, 8], [3, 6, 4], [8, 0, 4]
                ]

train_labels_a = [ 
                    293, 192, 291, 4, 0, 241, 231, 15, 273, 2,
                    254, 333, 262, 365, 293, 5, 277, 362, 147, 171
                ]

train_images = np.array(train_images_a, dtype=int)
# train_images = np.reshape(train_images,(20,3))
train_labels = np.array(train_labels_a) 

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(3,)),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(400)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=100)

model.save('ai1_talent.h5')

predicted_result = model.predict(train_images)



for idx, img in enumerate(train_images):
    i1 = input1[int(img[0])]
    i2 = input2[int(img[1])]
    i3 = input3[int(img[2])]
    
    print(predicted_result[idx])
    ai_label = np.argmax(predicted_result[idx])
    
    if ai_label < 10:
        ai_label = "00" + str(ai_label)
    elif ai_label < 100 and ai_label > 9:
        ai_label = "0" + str(ai_label)
    
    id1 = str(ai_label)[0]
    id2 = str(ai_label)[1]
    id3 = str(ai_label)[2]
        
    o1 = output1[int(id1)]
    o2 = output2[int(id2)]
    o3 = output3[int(id3)]
    
    result = f"""
    ----------------------------------------------------------------------------------------------------------------------
    "{i1} 업종", "{i2}년 사이의 연차", "{i3}점 수준의 학점 정보"에 따른 인재로는 ↓
    
    "{o1} 학위", "{o2} 학과", "{o3}"세 연령대의 조건을 가진 사람이 적합하다고 판단하여 추천합니다. 
    ----------------------------------------------------------------------------------------------------------------------
    """
    print(result)





