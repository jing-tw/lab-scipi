#coding=utf-8

from numpy import genfromtxt
import numpy as np  # for mean

Array2D = genfromtxt('my_file.csv', delimiter=',')

# get an entire column
Col0= Array2D[:,0]
print "Array2D=", Array2D 
print "Col0=",Col0 
print "mean=",np.mean(Col0)
