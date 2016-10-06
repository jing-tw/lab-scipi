# -*- coding: utf-8 -*-

from numpy import genfromtxt
Array2D = genfromtxt('my_file.csv', delimiter=',')

# get an entire column
Col0_20_Sample= Array2D[1:19,0]
print "Array2D=", Array2D
print "Col0_20_Sample=",Col0_20_Sample
