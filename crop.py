import cv2
import numpy as np

"""
	Area specifications in cv2.contourArea() in the if statements of blob() and edge_detection()
	must be set depending on the sizes of the original image and the post-its. 
"""
#approx1 in def blob() returns the vertices of the square post-its in an un-uniform clockwise manner.
#This function standardizes the arrangement of vertices and gets rid of unwanted boundaries around the post-its
def get_square(square):
	#organise
	min_row = square[::,::,1::].min()
	max_row = square[::,::,1::].max()
	min_col = square[::,::,0:1:].min()
	max_col = square[::,::,0:1:].max()
	mean_row = (min_row+max_row)/2
	mean_col = (min_col+max_col)/2


	col0 = square[0,0,0]
	row0 = square[0,0,1]
	col1 = square[1,0,0] 
	row1 = square[1,0,1] 
	col2 = square[2,0,0]
	row2 = square[2,0,1] 
	col3 = square[3,0,0] 
	row3 = square[3,0,1] 


	#organise 
	#Our standard:The first vertex is the top right one.
	#The we go counter clockwise for the other vertices

	#if first vertex is at top left corner.
	if square[0][0][0]<mean_col and square[0][0][1]<mean_row:
		
		square[0,0,0] = col3
		square[0,0,1] = row3
		square[1,0,0] = col0
		square[1,0,1] = row0
		square[2,0,0] = col1
		square[2,0,1] = row1
		square[3,0,0] = col2
		square[3,0,1] = row2
	
	#if first vertex is at bottom left corner.
	if square[0][0][0]<mean_col and square[0][0][1]>mean_row:

		square[0,0,0] = col2
		square[0,0,1] = row2
		square[1,0,0] = col3
		square[1,0,1] = row3
		square[2,0,0] = col0
		square[2,0,1] = row0
		square[3,0,0] = col1
		square[3,0,1] = row1
		

	#if first vertex is at bottom right corner.
	if square[0][0][0]>mean_col and square[0][0][1]>mean_row:

		square[0,0,0] = col1
		square[0,0,1] = row1
		square[1,0,0] = col2
		square[1,0,1] = row2
		square[2,0,0] = col3
		square[2,0,1] = row3
		square[3,0,0] = col0
		square[3,0,1] = row0


	if square[0][0][1]>square[1][0][1]:
		square[1][0][1] = square[0][0][1]
	else:
		square[0][0][1] = square[1][0][1]	

	if square[2][0][1]>square[3][0][1]:
		square[2][0][1] = square[3][0][1]
	else:
		square[3][0][1] = square[2][0][1]	

	if square[1][0][0]>square[2][0][0]:
		square[2][0][0] = square[1][0][0]
	else:
		square[1][0][0] = square[2][0][0]	

	if square[0][0][0]>square[3][0][0]:
		square[0][0][0] = square[3][0][0]
	else:
		square[3][0][0] = square[0][0][0]	

	return square


#Detect edges using Canny and draws contours around the squares
#cv2.contourArea() is used to ignore small unnecessary squares.
#cv2.GaussianBlur() and cv2.dilate() are used to remove noise.
#'img' must be in HSV format.
#The function returns an HSV image with a white boundary around the post-its. 
def edge_detection(img):
	img = cv2.GaussianBlur(img,(5,5),0)
	for gray in cv2.split(img):
		canny  = cv2.Canny(gray,50,200)
		canny = cv2.dilate(canny,None,iterations = 1)
		conts,hier = cv2.findContours(canny,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in conts:
			approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
			if len(approx)==4 and cv2.contourArea(cnt) > 2000:
				cv2.drawContours(img,[cnt],0,(255,255,255),2)
				print cv2.contourArea(cnt)

	return img				


#'img' must be in HSV format
def blob(img,original_image):

	#Color blobbing for blue in opencv hsv format.
	BLUE_MIN = np.array([85, 10, 10],np.uint8)
	BLUE_MAX = np.array([130, 200, 200],np.uint8)
	blue_threshed = cv2.inRange(img, BLUE_MIN, BLUE_MAX)

	#Color blobbing for pink in opencv hsv format.
	PINK_MIN = np.array([150, 40, 40],np.uint8)
	PINK_MAX = np.array([200, 255, 255],np.uint8)
	pink_threshed = cv2.inRange(img	, PINK_MIN, PINK_MAX)

	#'threshed' is  a binary image with a defined outline of all the post-its .
	threshed = blue_threshed + pink_threshed
	cv2.imwrite('result10.jpg',threshed)

	contours, hierarchy = cv2.findContours(threshed,1, 2)
	noOfPostIts = 0

	for cnt in contours:
		approx1 = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
		if len(approx1)==4 and cv2.contourArea(cnt) > 2000:
			cv2.drawContours(threshed,[cnt],0,(255,255,255),2)
			#At this point, 'threshed' will be an image that identifies only the post-its.
			#This can be used to verify that the correct post-its will be cropped.
			square1 = approx1
			print cv2.contourArea(cnt)
			noOfPostIts += 1
			square1 = get_square(square1)
			temp_post = original_image[square1[1][0][1]:square1[2][0][1]:1,square1[1][0][0]:square1[0][0][0]:1,::]
			post_name = 'k' * noOfPostIts + '.jpg'
			#Save cropped post-its in the working directory.
			cv2.imwrite(post_name,temp_post)
			#cv2.imwrite(post_name,temp_post,[int(cv2.IMWRITE_JPEG_QUALITY), 90])
	print noOfPostIts
	return threshed

#cv2.imwrite('img.jpg',threshed)


#Read image from which post-its will be cropped.
im_2_crop = cv2.imread('IMG-20130110-00370.jpg')
#im_2_crop = cv2.imread('bp.jpg')

#Convert to HSV color space.
img = cv2.cvtColor(im_2_crop,cv2.COLOR_BGR2HSV)

#img = edge_detection(img)
#cv2.imwrite('result11.jpg',img)
#print '\n'
img = blob(img,im_2_crop)
cv2.imwrite('result12.jpg',img)
