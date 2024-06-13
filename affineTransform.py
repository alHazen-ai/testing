'''
import cv2
import numpy as np

image = cv2.imread('test.jpeg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Store height and width of the image

width, height = imgGray.shape

center = width/2, height/2

#       | 1 0 Tx |
#  R  = | 0 1 Ty |
print(center)
# T is our translation matrix
T = np.float32([[1, 0, 70], [0, 1, 30]])
imgTranslate = cv2.warpAffine(imgGray, T, (width, height))

# We use warpAffine to transform the image using the matrix, T
R = cv2.getRotationMatrix2D(center, 70, 1)
img_rotateScale = cv2.warpAffine(imgGray, R, (width, height))
print(R)
imgFlip = cv2.flip(imgGray, 1)


cv2.imshow("Translate", imgTranslate)
cv2.imshow("Rotation and Scale", img_rotateScale)
cv2.imshow("Fliped", imgFlip)

cv2.waitKey()
cv2.destroyAllWindows()
'''

# example applying affine transformation

import cv2
import numpy as np

img = cv2.imread('test.jpeg')
rows, cols = img.shape[:2]

src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[0,0], [int(0.6*(cols-1)),0], [int(0.4*(cols-1)),rows-1]])
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols,rows))

cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.waitKey()