from preprocess import preprocess, detect_text, localize
from predictor import prediction
import numpy as np
import matplotlib.pyplot as plt
import cv2

def recognition(gray_image, show):
    segments, template, th_img, text_color = preprocess(gray_image)
    labels = []
    show_img = gray_image[:]
    #print(len(segments))
    
    for segment in segments: 
        #plt.imshow(segment)
        #plt.show()
        recimg, bimg = detect_text(show_img, th_img, segment, text_color)
        #print('Process: Recognition....\n')
        label= prediction(bimg)
        labels.append(str(label))
        show_img = localize(show_img, th_img, segment, text_color, show)
        char = labels
    char = ''.join(char)
            
    if (show == 'show'):
        plt.imshow(show_img)
        plt.title('Detecting')
        plt.xticks([])
        plt.yticks([])
        plt.show()
    else:
        cv2.imshow('Detecting..', cv2.cvtColor(show_img, cv2.COLOR_GRAY2BGR))
img=cv2.imread("123.jpg")   
recognition(img,'show')  
    
    #plt.imshow(cv2.cvtColor(show_img, cv2.COLOR_GRAY2RGB))
    #plt.show()