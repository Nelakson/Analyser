import numpy as np
import cv2
import math

#Opencv does not returns vertices in a unique order.
#This function brings about a known order;
#TOP LEFT - TOP RIGHT - BOTTOM RIGHT - BOTTOM LEFT.

def rectify(h):
  h = h.reshape((4,2))
  hnew = np.zeros((4,2),dtype = np.float32)

  add = h.sum(1)
  hnew[0] = h[np.argmin(add)]
  hnew[2] = h[np.argmax(add)]

  diff = np.diff(h,axis = 1)
  hnew[1] = h[np.argmin(diff)]
  hnew[3] = h[np.argmax(diff)]
  return hnew

#This function addresses the skewness of post-its.
#Argument 'skew_im' is an outline of a post-it along the vertices.
def get_square(skew_im, name):

	skew_im_copy = skew_im.copy()
	skew_im_copy = cv2.cvtColor(skew_im_copy,cv2.COLOR_BGR2HSV)	
	warp = cv2.resize(skew_im,(450,450))

	if name == 'be':
		BLUE_MIN = np.array([80, 65, 60],np.uint8)
		BLUE_MAX = np.array([130, 255, 255],np.uint8)
		threshed = cv2.inRange(skew_im_copy, BLUE_MIN, BLUE_MAX)

	if name =='pe':
		PINK_MIN = np.array([120, 50, 50],np.uint8)
		PINK_MAX = np.array([180, 255, 255],np.uint8)
		threshed = cv2.inRange(skew_im_copy , PINK_MIN, PINK_MAX)

	if name == 'ge':
		GREEN_MIN = np.array([35, 60, 60],np.uint8)
		GREEN_MAX = np.array([80, 255, 255],np.uint8)
		threshed = cv2.inRange(skew_im_copy, GREEN_MIN, GREEN_MAX)
	
	#Only one post-it must be detected. Check this from noOfPostIts
	contours, hierarchy = cv2.findContours(threshed,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	
	noOfPostIts1 = 0
	for cnt in contours:
		approx1 = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
		if len(approx1)==4 and cv2.contourArea(cnt) > 100000:
			cv2.drawContours(threshed,[cnt],0,(255,255,255),2)
			my_approx = rectify(approx1)
			noOfPostIts1 += 1
			h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
			retval = cv2.getPerspectiveTransform(my_approx,h)
			warp = cv2.warpPerspective(skew_im,retval,(450,450))
	if noOfPostIts1 != 1:
		print 'CHECK DUDE. ' + name	

	return warp


#Find post-Its and save them.
def square_contours(threshed_image,original,name):

	contours, hierarchy = cv2.findContours(threshed_image,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	noOfPostIts = 0

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
		if len(approx)==4 and cv2.contourArea(cnt) > 100000:
			cv2.drawContours(threshed_image,[cnt],0,(255,255,255),2)
			square = approx
			square = rectify(square)
			min_row = square[::,1::].min()
			max_row = square[::,1::].max()
			min_col = square[::,0:1:].min()
			max_col = square[::,0:1:].max()
			skew = original[min_row:max_row:, min_col:max_col: , ::]
			noOfPostIts += 1
			temp_post = get_square(skew,name)
			post_name = name * noOfPostIts + '.jpg'
			cv2.imwrite(post_name,temp_post)
	return threshed_image,noOfPostIts


def blue_blobs(hsv_img,original):
	
	#Color blobbing for blue in opencv hsv format.
	BLUE_MIN = np.array([80, 65, 60],np.uint8)
	BLUE_MAX = np.array([130, 255, 255],np.uint8)
	blue_threshed = cv2.inRange(hsv_img, BLUE_MIN, BLUE_MAX)
	#Noise removal
	blue_threshed = cv2.medianBlur(blue_threshed,15)
	cv2.imwrite('blue.jpg',blue_threshed)
	b_name = 'be'
	b_threshed,blues = square_contours(blue_threshed , original , b_name)
	cv2.imwrite('blue_contours.jpg',b_threshed)
	print blues
	return b_threshed

def pink_blobs(hsv_img,original):
	
	#Color blobbing for pink and purple in opencv hsv format.
	PINK_MIN = np.array([120, 50, 50],np.uint8)
	PINK_MAX = np.array([180, 255, 255],np.uint8)
	pur_pink_threshed = cv2.inRange(hsv_img	, PINK_MIN, PINK_MAX)
	#Noise removal 
	pur_pink_threshed = cv2.medianBlur(pur_pink_threshed,15)
	cv2.imwrite('purpink.jpg',pur_pink_threshed)
	p_name = 'pe'
	p_threshed,purpinks = square_contours(pur_pink_threshed , original, p_name)
	cv2.imwrite('purpink_contours.jpg',p_threshed)
	print purpinks
	return p_threshed

def green_blobs(hsv_img,original):
	
	#Color blobbing for green in opencv hsv format.
	GREEN_MIN = np.array([35, 60, 60],np.uint8)
	GREEN_MAX = np.array([80, 255, 255],np.uint8)
	green_threshed = cv2.inRange(hsv_img, GREEN_MIN, GREEN_MAX)
	#Noise removal
	green_threshed = cv2.medianBlur(green_threshed,15)
	cv2.imwrite('green.jpg',green_threshed)
	g_name = 'ge'
	g_threshed,greens = square_contours(green_threshed , original, g_name)
	cv2.imwrite('green_contours.jpg',g_threshed)
	print greens
	return g_threshed


def blob(img):

	original = img.copy()
	img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)	
	blue_blobs(img,original)
	#cv2.waitKey()
	pink_blobs(img,original)
	#cv2.waitKey()
	green_blobs(img,original)


#Read image from which post-its will be cropped.
im_2_crop = cv2.imread('IMG-20130110-00369.jpg')
#im_2_crop = cv2.imread('bbbbbb.jpg')
#im_2_crop = cv2.resize(im_2_crop, (000,2000))
#cv2.imwrite('sized.jpg',im_2_crop)
img = blob(im_2_crop)