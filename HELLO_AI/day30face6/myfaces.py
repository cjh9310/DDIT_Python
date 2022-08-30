import cv2
import random
import numpy as np


labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        
        "05",
        "06",
        "07",
        "08",
        "09",
        
        "10",
        "11",
        "12",
        "13",
        "14",
        
        "15",
        "16",
        "17",
        "18",
        "19",
        
        "20",
        "21",
        "22"
      ]



img = np.empty((0, 0, 0), np.uint8)

img1 = cv2.imread("train_image/00/0.png")
img2 = cv2.imread("train_image/00/1.png")
img3 = cv2.imread("train_image/00/2.png")


img = np.append(img, img1)
img = np.append(img, img2)
img = np.append(img, img3)

img = img.reshape((3, 32, 32, 3))

cv2.imshow('img', img[1])

print(img1.shape)
print(img2.shape)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

# test_images
# test_label
# train_label

# import glob
    # path = './Freestyle2/*'
    # file_list = glob.glob(path)
    #
    # for file in file_list:
    #     file_name = str(file).replace('./Freestyle2\\','')
    #     file_name = "Freestyle2/" + file_name
    #     print(file_name)
    #     rg = RaoGibo(file_name)


# def saveImage(label,dir,reverse):
#     try:
#         vidcap = cv2.VideoCapture('movie/{}.mp4'.format(label))
#
#         count = 0
#         while(vidcap.isOpened()):
#             ret, src = vidcap.read()
#
#             height, width, channel = src.shape
#             matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
#             dst = cv2.warpAffine(src, matrix, (width, height))
#
#             print(dst.shape)
#             img_save = None
#             if reverse:
#                 img_save = dst
#             else:
#                 img_save = src
#
#             path ="";
#
#             if random.random() > 0.16:
#                 path = "train_image"
#             else:
#                 path = "test_image"
#
#
#             cv2.imwrite("{}/{}/{}.png".format(dir,count), img_save)
#
#             count += 1
#             # if count > 5:
#             #     break
#
#         vidcap.release()
#
#     except:
#         pass    
#
# for i in range(23):
#     pass



