#This code analysis the similarity between Post-Its 
#taken under different lighting conditions.


import cv2
import numpy as np

const_step = 80

#Returns the number of dark/black pixels in each 5X5 grid
#The two commented lines can replace the actual code,to enhance speed
#since for loops take time. 
def blackCount(im):
	#row, col = im.shape[:2]	
	b = 0
	for x in range(const_step):
		for y in range(const_step):
			if im[x,y] != 255:
				b += 1 
	#return row*col - cv2.countNonZero(im)
	return b

#Return normalized version of signatures(between 0 and 1)	
def normalize_signature(sign):
	return (sign-sign.min()) / (sign.max() - sign.min())


#5X5 grid of 400X400 image. Returns the image signature(1D array with 25 elements)
#Image shape must be square and dimensions must be a multiple of 5
def grid_signature(im):
	im_sign = np.zeros(25)
	for i in range(5):
		for j in range(5):
			im_temp = im[i*const_step:i*const_step + const_step:1 , j*const_step:j*const_step + const_step:1]	# 5X5 grid extract
			im_sign[i*5 + j] = blackCount(im_temp)
	im_sign = normalize_signature(im_sign)		
	return im_sign		


#Gets the signatures and checks for similarity
#Returns True for similar and False otherwise.
def compare(sign1,sign2):
	diff = abs(sign1-sign2)
	if diff.max() > 0.4:
		print ' not similar '
		return False
	else:
		print ' similar '			
		return True

#Reads and converts a color image to grayscale, then to black and white. 
#Also resizes the image. We process 400X400 square images.
def image_preprocessing(imageFilename):
	image = cv2.imread(imageFilename)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#Conversion to black and white.
	(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	im_bw = cv2.resize(im_bw,(400,400))
	return im_bw

#im1 and im2 are examples of some post-its. Try with some other examples as well.
#im1 = image_preprocessing('blue1b.jpg')
#im2 = image_preprocessing('pink1b.jpg')
#compare(grid_signature(im1), grid_signature(im2))





