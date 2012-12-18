import cv2
import cv
import numpy as np
from PIL import Image
import os
import math

def norm_image(im,dim):				# dim is used to resize the image to a square.
	im = cv2.resize(im, (dim,dim))
	im1 = im.astype(float)	
	for x in range(dim):
		for y in range(dim):
			norm = (im1[x,y,0]**2 + im1[x,y,1]**2 + im1[x,y,2]**2)**0.5
			if norm != 0:
				im1[x,y,0] = (im1[x,y,0] / norm) 
				im1[x,y,1] = (im1[x,y,1] / norm) 
				im1[x,y,2] = (im1[x,y,2] / norm) 
			#still have to code for peach black (0,0,0,) pixels.
	return im1

def bgr_mean(im,dim):
	#im1 = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
	b=0.0
	g=0.0
	r=0.0
	for x in range(dim):
		for y in range(dim):
			b += im[x,y,0] 
			g += im[x,y,1]
			r += im[x,y,2]
	#the means
	return b,g,r		 




def signature_4X4(im,dim): 	#dim must be greater than 4 and a multiple of 4.
	im_sign = np.ones(48)
	step = dim/4
	im = norm_image(im,dim)
	for i in range(4):
		for j in range(4):
			bgr_indexer = i*12 + j*3
			im_temp = im[i*step:i*step + step:1 , j*step:j*step + step:1 , 0:3:1]
			im_sign[bgr_indexer], im_sign[bgr_indexer + 1], im_sign[bgr_indexer + 2] = bgr_mean(im_temp,step)
	return im_sign



im1 = cv2.imread('post1a.jpg')
post1a = signature_4X4(im1,400)
#print post1a
im2 = cv2.imread('test.jpg')
post1b = signature_4X4(im2,400)
#print post1b


def compare_signatures(sign1,sign2): # returns true(1) if the images are similar and false(0) otherwise. 
 	similar = 1
 	a = abs(sign1-sign2) < 500  	# create a boolean array with same dim as sign1&2
 	print a
 	i = 0
	while i<48:
		print i
		if a[i] == 0: 
			similar = 0
		i = i + 1	
	return similar


#print compare_signatures(post1a, post1b)