import os
from shutil import copyfile

files = os.listdir("train")

for f in files:
    sub_files = os.listdir("train/"+f)
    for idx,sf in enumerate(sub_files):
        print(f,idx,sf)
        copyfile(f'train/{f}/{sf}',f'train_eng/{f}/{idx}.png')