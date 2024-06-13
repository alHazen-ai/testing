import cv2
import numpy as np

# Function we'll use to display contour area
def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas


# Let's load a simple image with 3 black squares
#image = cv2.imread('shapes.jpg')
image = cv2.imread('crateOfBottles.png')

original_image = image
# Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (7,7), 0)

#gray = cv2.medianBlur(gray, 7)

#Original Image
cv2.imshow('Input Image', image)
cv2.waitKey(0)



# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

edged = cv2.dilate(edged, None,iterations=4)
cv2.imshow("After Dilation", edged)
cv2.waitKey(0)

edged = cv2.erode(edged, None,iterations=11)
cv2.imshow("After Eroison", edged)
cv2.waitKey(0)
'''
edged = cv2.dilate(edged, None,iterations=2)
cv2.imshow("Final", edged)
cv2.waitKey(0)
'''
# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Let's print the areas of the contours before sorting

print("Contor Areas before sorting")
print(get_contour_areas(contours))
allAreas = get_contour_areas(contours)
print(allAreas[1])
counter = 0

for cnt in contours:
    print("cnt", cnt)
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    print("Approx", approx)
    if len(approx) >= 8:# & cnt > 1:
        cv2.drawContours(image, [cnt], 0, (0, 255, 255), -1)
        counter = counter + 1

# Sort contours large to small
#sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
#sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

print("Contor Areas after sorting")
#print(get_contour_areas(sorted_contours))
print(counter, " number of bottles")
# Iterate over our contours and draw one at a time
#for c in sorted_contours:
#   cv2.drawContours(original_image, [c], -1, (255,0,0), 3)
#    cv2.imshow('Contours by area', original_image)
#    cv2.waitKey(0)
cv2.imshow("final", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
