import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('coinCount.jpg')
#image = cv2.imread('images/shapes_donut.jpg')

# Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#Original Image
cv2.imshow('Input Image', image)
cv2.waitKey(0)


# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0), 3)

print("Number of Contours found = " + str(len(contours)))
print('contours', contours)
print('hierarchy',hierarchy)
print("Total of ", len(contours), "Coins")
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()