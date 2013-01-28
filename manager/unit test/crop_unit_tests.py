import pytest
import cv2
import numpy as np
from test import *

#def test_function3():
#	assert image_preprocessing('pink1a.jpg').max() == 255
#	assert image_preprocessing('pink1a.jpg').min() == 0

name1 = '1a.jpg'
name2 = '2a.jpg'
name3 = '3a.jpg'
name4 = '4a.jpg'
name5 = '5a.jpg'
name6 = '6a.jpg'
name7 = '7a.jpg'
name8 = '8a.jpg'
name9 = '9a.jpg'
name10 = '10a.jpg'
name11 = '11a.jpg'

def test_combination1():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('1.jpg'))) == True
def test_combination2():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination3():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination4():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination5():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination6():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination7():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination8():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination9():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination10():
	assert compare(grid_signature(image_preprocessing(name1)), grid_signature(image_preprocessing('10.jpg'))) == False
#def test_combination11():
#	assert compare(grid_signature(image_preprocessing('blue2a.jpg')), grid_signature(image_preprocessing('bebe2.jpg'))) == False
#def test_combination12():
#	assert compare(grid_signature(image_preprocessing('bebe2.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == False
#def test_combination13():
#	assert compare(grid_signature(image_preprocessing('be1.jpg')), grid_signature(image_preprocessing('bebebe2.jpg'))) == False
#def test_combination14():
#	assert compare(grid_signature(image_preprocessing('bebebe2.jpg')), grid_signature(image_preprocessing('bebebe1.jpg'))) == True
#def test_combination15():
#	assert compare(grid_signature(image_preprocessing('pe2.jpg')), grid_signature(image_preprocessing('pink1b.jpg'))) == True	

def test_combination11():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination12():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('2.jpg'))) == True
def test_combination13():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination14():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination15():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination16():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination17():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination18():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination19():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination20():
	assert compare(grid_signature(image_preprocessing(name2)), grid_signature(image_preprocessing('10.jpg'))) == False




def test_combination21():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination22():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination23():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('3.jpg'))) == True
def test_combination24():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination25():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination26():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination27():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination28():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination29():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination30():
	assert compare(grid_signature(image_preprocessing(name3)), grid_signature(image_preprocessing('10.jpg'))) == False



def test_combination31():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination32():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination33():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination34():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('4.jpg'))) == True
def test_combination35():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination36():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination37():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination38():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination39():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination40():
	assert compare(grid_signature(image_preprocessing(name4)), grid_signature(image_preprocessing('10.jpg'))) == False	



def test_combination41():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination42():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination43():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination44():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination45():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('5.jpg'))) == True
def test_combination46():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination47():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination48():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination49():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination50():
	assert compare(grid_signature(image_preprocessing(name5)), grid_signature(image_preprocessing('10.jpg'))) == False



def test_combination61():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination62():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination63():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination64():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination65():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination66():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination67():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('7.jpg'))) == True
def test_combination68():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination69():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination70():
	assert compare(grid_signature(image_preprocessing(name7)), grid_signature(image_preprocessing('10.jpg'))) == False



def test_combination71():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination72():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination73():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination74():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination75():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination76():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination77():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination78():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('8.jpg'))) == True
def test_combination79():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination80():
	assert compare(grid_signature(image_preprocessing(name8)), grid_signature(image_preprocessing('10.jpg'))) == False



def test_combination81():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination82():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination83():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination84():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination85():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination86():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination87():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination88():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination89():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('9.jpg'))) == True
def test_combination90():
	assert compare(grid_signature(image_preprocessing(name9)), grid_signature(image_preprocessing('10.jpg'))) == False



def test_combination91():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination92():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination93():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination94():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination95():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination96():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination97():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination98():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination99():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination100():
	assert compare(grid_signature(image_preprocessing(name10)), grid_signature(image_preprocessing('10.jpg'))) == True



def test_combination101():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('1.jpg'))) == False
def test_combination102():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('2.jpg'))) == False
def test_combination103():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('3.jpg'))) == False
def test_combination104():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('4.jpg'))) == False
def test_combination105():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('5.jpg'))) == False
def test_combination106():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('6.jpg'))) == False
def test_combination107():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('7.jpg'))) == False
def test_combination108():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('8.jpg'))) == False
def test_combination109():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('9.jpg'))) == False
def test_combination110():
	assert compare(grid_signature(image_preprocessing(name11)), grid_signature(image_preprocessing('10.jpg'))) == False	


def test_combination51():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('1.jpg'))) == False	
def test_combination52():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('2.jpg'))) == False	
def test_combination53():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('3.jpg'))) == False		
def test_combination54():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('4.jpg'))) == False	
def test_combination55():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('5.jpg'))) == False	
def test_combination56():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('6.jpg'))) == True
def test_combination57():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('7.jpg'))) == False	
def test_combination58():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('8.jpg'))) == False	
def test_combination59():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('9.jpg'))) == False	
def test_combination60():
	assert compare(grid_signature(image_preprocessing(name6)), grid_signature(image_preprocessing('10.jpg'))) == False					
