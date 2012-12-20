import pytest
import cv2
import numpy as np
from test import *

def test_function3():
	assert image_preprocessing('pink1a.jpg').max() == 255
	assert image_preprocessing('pink1a.jpg').min() == 0

def test_combination1():
	assert compare(grid_signature(image_preprocessing('blue1a.jpg')), grid_signature(image_preprocessing('blue1b.jpg'))) == True
def test_combination2():
	assert compare(grid_signature(image_preprocessing('blue1a.jpg')), grid_signature(image_preprocessing('blue2a.jpg'))) == False
def test_combination3():
	assert compare(grid_signature(image_preprocessing('blue1a.jpg')), grid_signature(image_preprocessing('blue2b.jpg'))) == False
def test_combination4():
	assert compare(grid_signature(image_preprocessing('blue1a.jpg')), grid_signature(image_preprocessing('pink1a.jpg'))) == False
def test_combination5():
	assert compare(grid_signature(image_preprocessing('blue1a.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == False
def test_combination6():
	assert compare(grid_signature(image_preprocessing('blue1b.jpg')), grid_signature(image_preprocessing('blue2a.jpg'))) == False
def test_combination7():
	assert compare(grid_signature(image_preprocessing('blue1b.jpg')), grid_signature(image_preprocessing('blue2b.jpg'))) == False
def test_combination8():
	assert compare(grid_signature(image_preprocessing('blue1b.jpg')), grid_signature(image_preprocessing('pink1a.jpg'))) == False
def test_combination9():
	assert compare(grid_signature(image_preprocessing('blue1b.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == False
def test_combination10():
	assert compare(grid_signature(image_preprocessing('blue2a.jpg')), grid_signature(image_preprocessing('blue2b.jpg'))) == True
def test_combination11():
	assert compare(grid_signature(image_preprocessing('blue2a.jpg')), grid_signature(image_preprocessing('pink1a.jpg'))) == False
def test_combination12():
	assert compare(grid_signature(image_preprocessing('blue2a.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == False
def test_combination13():
	assert compare(grid_signature(image_preprocessing('blue2b.jpg')), grid_signature(image_preprocessing('pink1a.jpg'))) == False
def test_combination14():
	assert compare(grid_signature(image_preprocessing('blue2b.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == False
def test_combination15():
	assert compare(grid_signature(image_preprocessing('pink1a.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == True															