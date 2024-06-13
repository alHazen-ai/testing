# Harris Corner Detection Method

# organizing imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('breakfastCorner.png')
imgCopy = np.copy(image)

imgCopy = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB)
plt.imshow(imgCopy)
plt.show()

gray = cv2.cvtColor(imgCopy, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)
plt.imshow(gray)
plt.show()
'''
image = cv2.medianBlur(gray, 3)
cv2.imshow("after blurring", image)
cv2.waitKey(0)
image = cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,5)
cv2.imshow("After Adaptive Thresholding", image)
cv2.waitKey(0)
'''

# modify the data type
# setting to 32-bit floating point
#operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters

dest = cv2.cornerHarris(gray, 2, 5, 0.04)
dest = cv2.dilate(dest, None)

import matplotlib.pyplot as plt
plt.imshow(dest, cmap='gray')
plt.show()

image[dest > 0.1 * dest.max()]=[0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', image)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()