from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

ti1 = np.load("omok_train5.npy")
ti2 = np.load("omok_train5.npy")
ti3 = np.load("omok_train5.npy")
ti4 = np.load("omok_train5.npy")
ti5 = np.load("omok_train5.npy")

tl1 = np.load("omok_answer5.npy")
tl2 = np.load("omok_answer5.npy")
tl3 = np.load("omok_answer5.npy")
tl4 = np.load("omok_answer5.npy")
tl5 = np.load("omok_answer5.npy")


train_images = np.concatenate([ti1,ti2,ti3,ti4,ti5,ti1,ti2])
train_labels = np.concatenate([tl1,tl2,tl3,tl4,tl5,tl1,tl2])

np.save("train_images",train_images)

print(train_images.shape)
print(train_labels.shape)

train_labels_c = to_categorical(train_labels,num_classes=400)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(400,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(400, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images, train_labels_c, epochs=30)
model.save('alphao5.h5')

predict_result = model.predict(train_images)
print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    ii = int(ai_answer / 20)
    jj = ai_answer % 20
    print(ai_answer,ii,jj,end=",")
    print()



