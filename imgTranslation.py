import cv2
import numpy as np

img = cv2.imread("test.jpeg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(imgGray.shape)
width, height = imgGray.shape

Tx = width/2
Ty = height/2

T = [[1,0, Tx],
     [0, 1, Ty]]

T = np.float32(T)
imgTr = cv2.warpAffine(imgGray, T, (width, height))


cv2.imshow("original", img)
cv2.imshow("Translated", imgTr)

cv2.waitKey()
cv2.destroyAllWindows()
