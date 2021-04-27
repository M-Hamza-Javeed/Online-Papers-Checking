from django.conf import settings
import os,cv2
import re
import cv2 
import numpy as np
import tempfile
from PIL import Image


path=settings.MEDIA_ROOT

files=[]

def dirlist():
    for i in os.listdir(settings.MEDIA_ROOT):
        ext=i.split('.')
        files.append({"path":(path+"/"+i),"name":i,"extension":ext[len(ext)-1]})
    return files
    


def erode(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)


def thresholding(image):
    image = cv2.GaussianBlur(image,(3,3),0)
    image = cv2.threshold(image,0,200, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return image

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def set_image_dpi(im):
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300,300))
    return temp_filename


def imagefilter(image):
    img=settings.BASE_DIR+image
    image = Image.open(img)
    image = set_image_dpi(image)
    image = cv2.imread(image)
    image = cv2.resize(image,None,fx=3,fy=3,interpolation=cv2.INTER_AREA)  
    image = get_grayscale(image)
    image = thresholding(image)
    image = cv2.bilateralFilter(image,9,75,75)
    image = cv2.equalizeHist(image)
    crop=os.path.splitext(img)[0]+"-crop.png"
    cv2.imwrite(crop, image)
    return image
