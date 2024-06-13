import cv2
import numpy as np

image = cv2.imread('someshapes.jpg')
cv2.imshow('Original', image)

#image = cv2.blur(image,(3,3))
#image = cv2.medianBlur(image, 3)
#image = cv2.GaussianBlur(image, (7,7),0)
#image = cv2.fastNlMeansDenoising(image, None, 6, 6,21)
#image = cv2.bilateralFilter(image,9,70, 70)

# Create our shapening kernel, we don't normalize since the
# the values in the matrix sum to 1
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])
'''
kernel_sharpening = np.array([[-1,-1,-1,-1,-1],
                              [-1,-1,-1,-1,-1],
                              [-1,-1,25,-1,-1],
                              [-1,-1,-1,-1,-1],
                              [-1,-1,-1,-1,-1]])
'''
# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)
accumEdged = np.zeros(image.shape[:2], dtype="uint8")

for chan in cv2.split(image):
    # blur the channel, extract edges from it, and accumulate the set
    # of edges for the image
    chan = cv2.medianBlur(chan, 11)
    edged = cv2.Canny(chan, 50, 200)
    accumEdged = cv2.bitwise_or(accumEdged, edged)

# show the accumulated edge map
cv2.imshow("Edge Map", accumEdged)
cv2.waitKey(0)

contours = cv2.findContours(accumEdged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(accumEdged, contours, 2, (255,255,255), 3)
print(len(contours))

cv2.imshow("Contours on images", accumEdged)
cv2.waitKey(0)
cv2.destroyAllWindows()