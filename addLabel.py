from numpy import genfromtxt
import numpy as np



order = genfromtxt('label/orderTrainSet.csv', delimiter=',')
labels = genfromtxt('label/train.csv',delimiter=',')
y=np.array([])
k=1

for i in labels[:,0]:
    if (k == 2856): break
    if(i==order[k]):
        k+=1
        y = np.append(y, [labels[int(i)-1, 1]], 0)

print(y.shape)
np.savetxt("train/y.csv", y, delimiter=",")