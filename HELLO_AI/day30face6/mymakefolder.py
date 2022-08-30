import os


for i in range(100, 123):
    folder_name = str(i)[1:3]
    os.mkdir("train_image/" + folder_name)
