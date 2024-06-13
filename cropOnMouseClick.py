import cv2
import numpy as np

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
a=[]
b=[]

image = cv2.imread('test.jpeg')
height, width = image.shape[:2]

#cv2.namedWindow("image")
cv2.imshow("image", image)

cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

cv2.waitKey(0)

start_row=b[0]
end_row=b[1]
start_col=a[0]
end_col=a[1]

print(a, b)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row , start_col:end_col]
croppFixed = image[80:170, 77:180]

cv2.imshow("Fixed Crop Image", croppFixed) 
cv2.waitKey(0) 

cv2.imshow("Cropped Image", cropped) 
cv2.waitKey(0) 
cv2.destroyAllWindows()