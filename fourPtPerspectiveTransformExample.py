# import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	print(rect)
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped

if __name__== "__main__":
	image = cv2.imread('scan.jpg')

	# Cordinates of the 4 corners of the original image
	points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])
	#pts = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

    # Cordinates of the 4 corners of the desired output
	# We use a ratio of an A4 Paper 1 : 1.41
	points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

	# Use the two sets of four points to compute
	# the Perspective Transformation matrix, M

	M = cv2.getPerspectiveTransform(points_A, points_B)
	warped = cv2.warpPerspective(image, M, (420, 594))

	#pts = np.array(pts)

	#pts = np.array(eval(args["coords"]), dtype="float32")
	#apply the four point tranform to obtain a "birds eye view" of the image
	#warped = four_point_transform(image, pts)
	#show the original and warped images

	cv2.imshow("Original", image)
	cv2.imshow("Warped Perspective", warped)
	cv2.waitKey(0)
	cv2.destroyAllWindows()