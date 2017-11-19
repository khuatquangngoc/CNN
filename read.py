from numpy import genfromtxt
import numpy as np
from scipy.misc import imread


#+++++++++PARAMS+++++++++

#stride's params
input_size=32
field_size=5
stride=3
pad=0
filters=5

#image's params
image_height=32
image_width=32
image_depth=3
flatted_image_size=image_depth*image_depth*image_width

#data's params
number_examples=2856




#---------PARAMS---------


#+++++++++GENERATE DATA+++++++++


data = genfromtxt('train/data.csv', delimiter=',')
labels = genfromtxt()
data=data.reshape(number_examples, image_height, image_width, image_depth)#2856,32,32,3

y=

#---------GENERATE DATA---------


#+++++++++CONV+++++++++
def computeConv(data,filters):
    global W
    global b

    X=data.reshape(flatted_image_size,-1)

def conv(input_size=input_size,field_size=field_size,stride=stride,pad=pad,filters=filters,current_image):

    output_size = (input_size - field_size + 2 * pad) / stride + 1
    for i in range(0, input_size - field_size + 1, stride):  # +1 to take the last entry of range
        for j in range(0, input_size - field_size + 1, stride):
            window = data[current_image, i:i+5, j:j+5, 0:image_depth]
            computeConv(window)


#---------CONV---------



print(data[2855,:,:,:])






