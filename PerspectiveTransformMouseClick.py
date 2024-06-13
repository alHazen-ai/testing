# import the necessary packages
import cv2
import numpy as np

def on_EVENT_LBUTTONDOWN(event, x, y ,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        a.append(x)
        b.append(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, '+' , (x, y), font, fontScale=1, color=(255, 0, 0))
        cv2.imshow('Original', image)
        return x,y
a = []
b = []

image = cv2.imread('scan.jpg', 0)
image = cv2.resize(image, (image.shape), 0.5, 0.5)

cv2.imshow("Original", image)
cv2.setMouseCallback("Original", on_EVENT_LBUTTONDOWN)
cv2.waitKey(0)

# Cordinates of the 4 corners of the input image
points_A = np.float32([[a[0],b[0]],[a[1],b[1]], [a[2],b[2]], [a[3],b[3]]])

# Cordinates of the 4 corners of the desired output
# We use a ratio of an A4 Paper 1 : 1.41
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

print(a,b)

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M

M = cv2.getPerspectiveTransform(points_A, points_B)
warped = cv2.warpPerspective(image, M, (420, 594))


#cv2.imshow("Original", image)
cv2.imshow("Warped Perspective", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
