import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers
import cv2


labels_team = [ "최재혁", "박수현", "김유미", "박성우", "양형주", "이상권" ]

labels = [ "김유미", "박성우", "박수현", "양형주", "이상권", "최재혁" ]


for j in range(6):
    img1 = cv2.imread(f'mem{j}.jpg')
    
    resize_img = cv2.resize(img1, (128, 128))
    
    resize_img = np.reshape(resize_img, (1, 128, 128, 3))
    # train_images = np.load("train_image.npy")
    test_images = resize_img/255.0
    
    
    model = tf.keras.models.load_model('6face.h5')
    
    predictions = model.predict(test_images)
    
    for i in range(1):
        idx_label = np.argmax(predictions[i])
        print(labels_team[j]," -> ",  labels[idx_label])

