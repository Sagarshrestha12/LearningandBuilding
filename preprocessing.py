import cv2
import numpy as np
import argparse
def skew_correction(filename):
    image =cv2.imread(filename)
    # This is done by averaging the three chanel value
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # This is don by using simple techinque 255-value 
    #gray=cv2.bitwise_not(image)
    # binairze the image using thresholding 
    gray=cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    cv2.imshow("Bitwise_not and thresholding",thresh)
    cv2.waitKey(0)
    if angle <-45:
        angle= (90 +angle)
    else:
        angle = -angle
    # now applying affine transformation
    (h,w)=image.shape[:2]
    centre=(w//2,h//2)
    M=cv2.getRotationMatrix2D(centre,angle,1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def rescaleFrame(frame,scale =0.75):
    width=int(frame.shape[0]*scale)
    height =int(frame.shape[1]*scale)
    dimensions =(height,width)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
def color_detection(image):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask= mask1+mask2
    output = cv2.bitwise_and(image, image, mask = mask)
    output=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    output = cv2.threshold(output, 1, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return output
img=cv2.imread("my.jpeg")
cv2.imshow("skew_image",img)
img1=skew_correction("my.jpeg")
cv2.imshow("skew_corrected_image",img1)
cv2.waitKey(0)
rel=cv2.imread("saj.jpg")
blank=np.ones(rel.shape,dtype='uint8')*255
blank[:]=0,0,255
rel1= rescaleFrame(rel,scale=0.2)
img=rel[:,:,2]
img2=cv2.imread("ocen.jpeg")
img2=rescaleFrame(img2,scale=2)
cv2.imshow("blur",img2)
img2= cv2.GaussianBlur(img2,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("blur2",img2) 

#img=cv2.bitwise_and(rel,blank)
img =rescaleFrame(img,scale=0.2)
cv2.imshow('Blank',img)
cv2.imshow('Blank2',rel1)
height=rel1.shape[0]
widht=rel1.shape[1]
cropped=rel1[0:height//2,0:widht//2]
cropped=cv2.resize(cropped,(cropped.shape[1],cropped.shape[0]),interpolation=cv2.INTER_CUBIC)
cv2.imshow("croop",cropped)
cv2.waitKey(0)
img3=cv2.imread("numbers3.png")
img3= cv2.resize(img3,(24,24),interpolation=cv2.INTER_AREA)
cv2.imshow("fff",img3)
cv2.waitKey(0)
'''
cap =cv2.VideoCapture(0)
i=1
 while True:
    success ,img = cap.read()
    img= rescaleFrame(img,scale=0.4)
    cv2.imshow("video"+str(i),img)
    if cv2.waitKey(0):
        print(i)
        i+=1
    if 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

'''