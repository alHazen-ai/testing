import cv2
import numpy as np

#image = cv2.imread('test.jpeg')
image = cv2.imread('barcodes.jpg')
#imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Store height and width of the image
width, height = image.shape[:2]

center = width/2, height/2

imgLinearInterpolate = cv2.resize(image, (width, height), fx=0.75, fy=0.75)
cv2.imshow("Scaling with Linear Interpolation", imgLinearInterpolate)

imgCubicInterpolate =  cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling with Cubic Interpolation", imgCubicInterpolate)

imgSkewed = cv2.resize(image, (900, 400))
cv2.imshow("Scaling with Skewed Size", imgSkewed)

imgLinearInterpolate2 =  cv2.resize(image, None, fx=0.75, fy=1)
cv2.imshow("Scaling with Linear Interpolation 2", imgLinearInterpolate2)

cv2.waitKey()
cv2.destroyAllWindows()

'''
image = cv2.imread('test.jpeg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('Original', image )

cv2.imshow('Smaller ', smaller )
cv2.imshow('Larger ', larger )
cv2.waitKey(0)
cv2.destroyAllWindows()'''