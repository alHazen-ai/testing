import cv2
import numpy as np

image = cv2.imread('test.jpeg')

# Create a matrix of ones, then multiply it by a scaler of 100
# This gives a matrix with same dimesions of our image with all values being 100
M = np.ones(image.shape, dtype = "uint8") * 100

# We use this to add this matrix M, to our image
# Notice the increase in brightness
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Likewise we can also subtract
# Notice the decrease in brightness
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

addAgain = cv2.add(subtracted, added)
cv2.imshow("Repeat", addAgain)

cv2.waitKey(0)
cv2.destroyAllWindows()