import pyscreenshot as ImageGrab
from random import randint
import pyautogui
import time
import numpy as np
from scipy import misc
from numpy import *


ingredients = {"f_shrimp":(40,417), "f_rice":(110,410), "f_nori":(60,472), "f_roe":(110,470), "f_salmon":(41,540), "f_unagi":(90,547)}
stock = {"f_shrimp":5, "f_rice":10, "f_nori":10, "f_roe":10, "f_salmon":5, "f_unagi":5}


def clicks(x, y, b='left', clicks=5):
	pyautogui.moveTo(x,y)
	pyautogui.click(x=x, y=y, button='left', clicks=clicks)


def clearTable():
	clicks(55, 302)
	time.sleep(.1)
	clicks(105, 302)
	time.sleep(.1)
	clicks(205, 302)
	time.sleep(.1)
	clicks(305, 302)
	time.sleep(.1)
	clicks(405, 302)
	time.sleep(.1)
	clicks(505, 302)
	time.sleep(.1)
	clicks(605, 302)

def startGame():
	clicks(341, 306)
	time.sleep(2)
	clicks(440, 470)
	time.sleep(2)
	clicks(440, 484)
	time.sleep(2)
	clicks(601, 552)
	time.sleep(2)
	clicks(452, 464)

def buyrice():
	global stock
	clicks(560,390)
	time.sleep(1)
	clicks(579,365)
	time.sleep(1)
	clicks(529,388)
	time.sleep(1)
	stock["f_rice"] += 10

def buyroe():
	global stock
	clicks(580, 370)
	time.sleep(1)
	clicks(568,367)
	#530, 360 nori
	time.sleep(1)
	clicks(530,388)
	time.sleep(1)
	stock["f_roe"] += 10

def buynori():
	global stock
	clicks(580, 370)
	time.sleep(1)
	clicks(577,372)
	time.sleep(1)
	clicks(530,368)
	time.sleep(1)	
	stock["f_nori"] += 10

def killphone():
	clicks(607,444)
	time.sleep(1)

def takephone():
	clicks(617,470)
	time.sleep(1)

def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def rice():
	global stock
	stock["f_rice"] -=  1
	print(stock["f_rice"])

	if stock["f_rice"] <= 1:
		takephone()
		buyrice()
		killphone()

	clicks(ingredients["f_rice"][0], ingredients["f_rice"][1], clicks=1)
	time.sleep(1)

def nori():
	global stock
	stock["f_nori"] -= 1
	print(stock["f_nori"])

	if stock["f_nori"] <= 0:
		takephone()
		buynori()
		killphone()
	
	clicks(ingredients["f_nori"][0], ingredients["f_nori"][1], clicks=1)
	time.sleep(1)


def roe():
	global stock
	stock["f_roe"] -= 1
	print(stock["f_roe"])

	if stock["f_roe"] <= 1:
		takephone()
		buyroe()
		killphone()

	clicks(ingredients["f_roe"][0], ingredients["f_roe"][1], clicks=1)
	time.sleep(1)

def cook(food):
	if food == "gunkan":
		rice()
		time.sleep(1)
		nori()
		time.sleep(1)
		roe()
		time.sleep(1)
		roe()
		time.sleep(1)
		fold()
		time.sleep(1)

	elif food == "calroll":
		rice()
		time.sleep(1)

		nori()
		time.sleep(1)

		roe()
		time.sleep(1)
		fold()
		time.sleep(1)

	elif food == "onigiri":
		rice() 
		time.sleep(1)
		rice()
		time.sleep(1)
		nori()
		time.sleep(1)
		fold()
		time.sleep(1)

	

def order(seat):
	if seat == 1:
		im = ImageGrab.grab(bbox=(40,161,99,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")

	elif seat == 2:
		im = ImageGrab.grab(bbox=(140,161,199,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")


	elif seat == 3:
		im = ImageGrab.grab(bbox=(240,161,299,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")

	elif seat == 4:
		im = ImageGrab.grab(bbox=(340,161,399,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")


	elif seat == 5:
		im = ImageGrab.grab(bbox=(440,161,499,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")

	elif seat == 6:
		im = ImageGrab.grab(bbox=(640,161,699,176)) # X1,Y1,X2,Y2
		a = rgb2gray(np.array(im))
		sums = a.sum()
		print(sums)
		if sums >= 181000 and sums < 200765.477:
			print("calroll")
			cook("calroll")
		elif sums >= 130000 and sums < 150000:
			print("gunkan")
			cook("gunkan")
		elif sums >= 150000 and sums < 181000:
			print("onigiri")
			cook("onigiri")
		else:
			print("no order")


def fold():
	clicks(220, 534)
	time.sleep(.1)

if __name__ == "__main__":
	#print(pyautogui.press('enter'))
	#exit()
	clicks(220, 534)
	time.sleep(1)
	while True:	
		for i in range(1,7):
			print("Seat "+ str(i))
			order(i)
		clearTable()
