import numpy as np

from tensorflow import keras
from day28menu2db.daomenu import DaoMenu


dao = DaoMenu() 

labels = dao.getGroupMenu()

train_images_a = [
        [3,3 ]
]

train_images_n = np.array(train_images_a)
train_images_n = train_images_n / (len(labels)-1) 

model = keras.models.load_model('2.h5')

predictions = model.predict(train_images_n)

idx = np.argmax(predictions[0])

print(labels[idx])





