import cv2
import numpy as np

image = cv2.imread('test.jpeg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Store height and width of the image

width, height = imgGray.shape

center = width/2, height/2

R = cv2.getRotationMatrix2D(center,90,1)
print(R)
imgRotate = cv2.warpAffine(imgGray, R, (width, height))

imgRotate1 = cv2.transpose(imgGray)

imgFlip = cv2.flip(imgGray, 0)

cv2.imshow("Rotate", imgRotate)
cv2.imshow("Transposed", imgRotate1)
cv2.imshow("Fliped", imgFlip)

cv2.waitKey()
cv2.destroyAllWindows()