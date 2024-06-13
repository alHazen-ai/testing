# import the necessary packages
import numpy as np
import cv2
import imutils

def detect(image):
	# convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("test", img)
	cv2.waitKey(0)

	#	img = cv2.resize(image, image.shape, fx=0.75, fy=0.75)
	# gray = cv2.resize(gray, None, 1.2, 1.2, interpolation=cv2.INTER_CUBIC)

	# compute the Scharr gradient magnitude representation of the images
	# in both the x and y direction using OpenCV 2.4
	ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
	gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
	gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

	# subtract the y-gradient from the x-gradient
	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)
	cv2.imshow("gradient", gradient)
	cv2.waitKey(0)

	# blur and threshold the image
	blurred = cv2.blur(gradient, (9, 9))
	cv2.imshow("blurred", blurred)
	cv2.waitKey(0)
	(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

	# construct a closing kernel and apply it to the thresholded image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
	closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("closing", closed)
	cv2.waitKey(0)

	# perform a series of erosions and dilations
	closed = cv2.erode(closed, None, iterations=4)
	closed = cv2.dilate(closed, None, iterations=10)

	cv2.imshow("closed final", closed)
	cv2.waitKey(0)

	# find the contours in the thresholded image
	cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# if no contours were found, return None
	if len(cnts) == 0:
		return None
	# otherwise, sort the contours by area and compute the rotated
	# bounding box of the largest contour
	c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
	rect = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
	box = np.int0(box)

	# return the bounding box of the barcode
	return box


img = cv2.imread('barcodes.jpg')

img = imutils.resize(img, 512)

box = detect(img)

if box is not None:
	cv2.drawContours(img, [box], -1, (0, 255, 0), 2)

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# import the necessary packages
#from pyimagesearch import simple_barcode_detection
from imutils.video import VideoStream
import argparse
import time
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())
# if the video path was not supplied, grab the reference to the
# camera
if not args.get("video", False):
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
# otherwise, load the video
else:
	vs = cv2.VideoCapture(args["video"])

# keep looping over the frames
while True:
	# grab the current frame and then handle if the frame is returned
	# from either the 'VideoCapture' or 'VideoStream' object,
	# respectively
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
 
	# check to see if we have reached the end of the
	# video
	if frame is None:
		break
	# detect the barcode in the image
	box = detect(frame)
	# if a barcode was found, draw a bounding box on the frame
	if box is not None:
		cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
	# show the frame and record if the user presses a key
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# if we are not using a video file, stop the video file stream
if not args.get("video", False):
	vs.stop()
# otherwise, release the camera pointer
else:
	vs.release()
# close all windows 
cv2.destroyAllWindows()'''