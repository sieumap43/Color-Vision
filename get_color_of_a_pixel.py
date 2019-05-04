# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:39:12 2019

@author: Trieu Gia An
"""
#import neccessary libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
import colors as cl #custom library

color_arr = np.array([]) #an array to store all the Euclidean distances, the minimum distance is taken from this array

img_location = "sunflower.jpg" #image name

image = cv2.imread(img_location)                #read image from file
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #convert BGR colorspace to RGB colorspace

plt.imshow(image)   #show image
plt.show()

mid_col = int(image.shape[0]/2) #determine the indices of the middle pixel
mid_row = int(image.shape[1]/2)
mid_pixel = image[mid_col][mid_row] #store the RGB values of the middle pixel in mid_pixel variable

for i in range(cl.shape):   #calculate all the Euclidean distances
    color = cl.colors[i][1]
    color_arr = np.append(color_arr, math.sqrt(sum([(a - b)**2 for a, b in zip(mid_pixel, color)])))
   
index = color_arr.argmin()  #get the index of the smallest distance

print(cl.colors[index][0])  #the index of the smallest distance corresponds to the index of the name of the color in the chart