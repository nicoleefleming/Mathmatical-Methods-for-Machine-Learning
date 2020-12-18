import math
import matplotlib.pyplot as plt
import numpy as np

def func(L, v, offset):
    return (L**(-1.0/v)) + offset


xk = [4.8,2.3,2.4,1.8,4.7,1.8,0.6,3.8,2.0,1.3,2.1,0.4,0.5,4.8,4.8,2.9,0.1,1.2,1.8,4.3]
yk = [98.9,21.7,26.1,20.2,98.3,23.3,4.1,75.4,20.7,15.8,17.6,6.7,1.3,103.3,110.6,48.8,-2.4,17.4,23.1,81.5]

ones = np.ones(20)
xfeature = np.asarray(xk)
squaredfeature = xfeature ** 2
b = np.asarray(yk)

features = np.concatenate((np.vstack(ones),np.vstack(xfeature),np.vstack(squaredfeature)), axis = 1) # Change - remove the y values


determinants = np.linalg.lstsq(features, b)[0] # Change - use least squares

#Messy code to attempt to calculate the offset term
lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in lst:
    modelPredictions = func(*determinants + xk[i])
    #perform an analysis to get a change of data
    holder = modelPredictions - yk[i]
    #percentage of the holder
    holder = holder * 0.01
    print("Holder: ", holder)
    #calculate holder back to original value to get entire impact on system.
    holder = holder * 100
    # get the difference between yk and the calculated term
    absError = yk[i] + holder
    #print attempted calcuationof the offset term
    print(absError)

plt.scatter(xfeature,b)
u = np.linspace(-5,6,100)
plt.plot(u, u**2*determinants[2] + u*determinants[1] + determinants[0])

plt.show()

#Code for Curve Fit
#model = np.poly1d(np.polyfit(xk,yk,2))

#polyline = np.linspace(-5,6,100)
#plt.scatter(xk, yk)
#plt.plot(polyline, model(polyline))
#print(model)
#plt.show()

