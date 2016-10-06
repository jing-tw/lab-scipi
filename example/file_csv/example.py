#coding=utf-8

from numpy import genfromtxt
my_data = genfromtxt('my_file.csv', delimiter=',')

print my_data
