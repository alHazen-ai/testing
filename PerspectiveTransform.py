# import the necessary packages
import cv2
import numpy as np

'''
image = cv2.imread('ex2.jpg')
rows, cols, ch = image.shape

cv2.imshow('Original', image)
cv2.waitKey(0)

# Cordinates of the 4 corners of the original image
points_A = np.float32([[320, 15], [700, 215], [85, 610]])

# Cordinates of the 4 corners of the desired output
# We use a ratio of an A4 Paper 1 : 1.41
points_B = np.float32([[0, 0], [420, 0], [0, 594]])

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M
M = cv2.getAffineTransform(points_A, points_B)

warped = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow('warpPerspective', warped)
cv2.waitKey(0)
'''
image = cv2.imread('scan.jpg')
#width, height = image.shape[:2]
#print(width,height)
#image = cv2.resize(image,(width, height),0,0)
# Cordinates of the 4 corners of the original image


points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

# Cordinates of the 4 corners of the desired output
# We use a ratio of an A4 Paper 1 : 1.41
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M

M = cv2.getPerspectiveTransform(points_A, points_B)
warped = cv2.warpPerspective(image, M, (420, 594))

cv2.imshow("Original", image)
cv2.imshow("Warped Perspective", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.destroyAllWindows()