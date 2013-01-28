#This code analysis the similarity between Post-Its 
#taken under different lighting conditions.


import cv2
import numpy as np

const_step = 2 #im_size/5

#Returns the number of dark/black pixels in each 5X5 grid
#The two commented lines can replace the actual code,to enhance speed
#since for loops take time. 
def blackCount(im):
	row, col = im.shape[:2]	
	return row*col - cv2.countNonZero(im)

#Return normalized version of signatures(between 0 and 1)	
def normalize_signature(sign):
	return (sign-sign.min()) / (sign.max() - sign.min())

#5X5 grid of 400X400 image. Returns the image signature(1D array with 28 elements(25+3))
#Image shape must be square and dimensions must be a multiple of 5
def grid_signature(gray):
	mean_val = gray.mean()
	im_sign = np.zeros(64)
	for i in range(8):
		for j in range(8):
			if gray[i,j] > mean_val:
				im_sign[i*8 + j] = 1	  
	return im_sign		


#Gets the signatures and checks for similarity
#Returns True for similar and False otherwise.
def compare(sign1,sign2):
	print sign1
	print sign2
	diff = sign1+sign2
	#tolerance is the number of values greater than 0.4 in array diff.
	noOfDiff = diff[(diff == 1)].size
	print noOfDiff
	#print diff
	#cc =  np.corrcoef(sign1,sign2)[1,0]
	#print cc
	if noOfDiff > 30:
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
	#(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	gray = cv2.resize(gray,(8,8))
	return gray


def binarize(image):
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#Conversion to black and white.
	#(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	gray = cv2.resize(gray,(8,8))
	return gray

#im1 and im2 are examples of some post-its. Try with some other examples as well.
im1 = image_preprocessing('4a.jpg')
im2 = image_preprocessing('5.jpg')
compare(grid_signature(im1), grid_signature(im2))
