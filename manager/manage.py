import cv2
import numpy as numpy
import glob
import json
from test import *

list1 = glob.glob('day2/post?.jpg') + glob.glob('day2/post??.jpg')
list2 = glob.glob('day1/post?.jpg') + glob.glob('day1/post??.jpg')
list3 = glob.glob('day2/post?.json') + glob.glob('day2/post??.json')
list4 = glob.glob('day1/post?.json') + glob.glob('day1/post??.json')



def findAndTrack(list1,list2):
	sims = 0
	comps = 0
	for name1 in list1: # glob.glob('day2/post?.jpg'):
		#print name1
		count = 0
		im1 = cv2.imread(name1)
		sign1 = grid_signature(binarize(im1))
		for name2 in list2:
			#print name2
			im2 = cv2.imread(name2)
			sign2 = grid_signature(binarize(im2))
			comps +=1
			if compare(sign1,sign2) == True:
				json_name1 = name1[:-3] + 'json' #day2
				json_name2 = name2[:-3] + 'json' #day1
				print json_name2
				print json_name1
				f1 = open(json_name2,'r')
				j1 = json.load(f1)
				col = j1["column"]

				f2 = open(json_name1,'r')
				j2 = json.load(f2)
				new_col = j2["column"]

				if col==new_col:
					print name2 + ' has not moved.'
				else:
					print name2 + ' has moved'	

				count += 1
				sims +=1
		if count == 0:
			print name1 + ' is a new item'
		print '\n'	
	print sims	
	print comps					

findAndTrack(list1,list2)

	