from pioneer_sdk import Pioneer
from easy_ocr import ocr_image
import cv2

img = cv2.imread('images/ahleb.png')
img = cv2.Canny(img, 90, 90)
cv2.imshow('kuku', img)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(con)
cv2.waitKey(0)
