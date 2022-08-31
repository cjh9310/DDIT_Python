import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

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


def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.003:
            pass
        else:
            break
        idx_f+=1
        
    idx_f-=10
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.003:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=10
    
    return arr_n[idx_f:idx_l]


file_list = os.listdir("record")

for i in file_list:
    y, sr = librosa.load("record/"+i)

    y_trim = cutMute(y)
    
    t = np.arange(0, len(y_trim))
    print(sr)
    print(y_trim)
    
    plt.specgram(y_trim)
    plt.savefig("spectrum/{}.png".format(i[0:5]))





