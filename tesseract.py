
import cv2 
import pytesseract

img =cv2.imread('C:/Users/Hamza/project/papers/media/image.jpeg');
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))
