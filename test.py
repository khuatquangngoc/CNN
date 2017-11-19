import time
from scipy.misc import imread
import numpy as np

x=imread('train/image/1.png')
x=x.reshape(3072,-1)
t1=time()
y=np.ones(3072,-1)
z=np.dot(x.transpose,y)
t2=time()


print(t2-t1)
