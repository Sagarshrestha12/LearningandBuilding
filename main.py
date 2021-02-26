import cv2 
import numpy as np
from keras.models import model_from_json
from random import randint
from readdb import update_db,fetch
from pdfgenerate import create_pdf
img =cv2.imread('sam2.jpg',cv2.IMREAD_GRAYSCALE)
img=255-img
ret3,img= cv2.threshold(img,150,255,cv2.THRESH_BINARY)
proj = np.sum(img,1)
m=0
h=0
for i in range(len(proj)):
    if proj[i]>100:
        m=i-5
        break
for i in range(len(proj)-1,1,-1):
    if proj[i]>10:
        h=i+5
        break
height=h-m
hori_img=img[m:h,0:img.shape[1]]
kernel = np.ones((5,5),np.uint8)
upper=hori_img
cont_upper,_ = cv2.findContours(upper, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont_lower, _  = cv2.findContours(upper, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
def sort_contours(cnts,reverse = False):
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return cnts
mark=''
u =[]
if len(cont_upper) !=0:
  for c in sort_contours(cont_upper):
    # print(c)
    (x, y, w, h) = cv2.boundingRect(c)
    u.append([x,x+w,y,y+h])
    curr_num = upper[y:y+h,x:x+w]
    json_file = open('model.json', 'r')
    
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json) 
    loaded_model.load_weights("model.h5")
    dim=(28,28)
    x= cv2.resize(curr_num,dim,interpolation=cv2.INTER_AREA)
    x=np.expand_dims(x,2)
    x=np.expand_dims(x,0)
    y=np.argmax(loaded_model.predict(x), axis=-1)
    mark=mark+str(y[0])   
id= 10
update_db(id,mark)
all_info=fetch(id)
create_pdf(all_info)