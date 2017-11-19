import numpy as np


#W1=5,H1=5,D1=3
#K=2,F=3,S=2,P=1
#=> spatial size =3x3=E


#at each 3x3 blocks of pixels we stretch it into a vector size 3*3*3=27. and then the X_col input of us have 27*9
# the weights of conv layer are similarly stretched out into rows. if we take 10 filter layers therefore 10*(3*3*3)=10*27 matrix
#the activation map will have the dimension (10*27)*(27*9)=10*9
#and the must reshape in to 10*3*3

implement an a rray have the [x,y] position to slide. called A
i=0

W_row=tf.truncate(F*F*D1,K)

for x,y in A:
    X_col[:,i]=image([x,y]).reshape(F*F*D1,1)
    i++

X=(W_col*X_col).reshape(K,E,E)