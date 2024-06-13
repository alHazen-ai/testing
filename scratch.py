import cv2
import numpy as np

image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray win", gray)
cv2.waitKey(0)
