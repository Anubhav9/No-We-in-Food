import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2

def getPrediction(file):
	model = tf.keras.models.load_model('my_model.h5')
	img=cv2.imread(file)
	img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	resize=cv2.resize(img,(224,224))
	resize=resize/255.
	resize=np.expand_dims(resize,axis=0)
	print(resize)
	result=np.argmax(model.predict(resize))
	print(result)
	if(result==0):
		final_result='Chicken Curry'
	elif(result==1):
		final_result='Chicken Wings'
	elif(result==2):
		final_result='Fried Rice'
	elif(result==3):
		final_result='Grilled Salmon'
	elif(result==4):
		final_result='Hamburger'
	elif(result==5):
		final_result='Ice Cream'
	elif(result==6):
		final_result='Pizza'
	elif(result==7):
		final_result='Ramen'
	elif(result==8):
		final_result='Steak'
	elif(result==9):
		final_result='Sushi'
	return final_result