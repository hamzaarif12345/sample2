import numpy
from scipy import stats
s= []
f=int(input("Enter the number of elements in the lists:"))
for i in  range(0,f):
  x=int(input("enter the number "))
  s.append(x)
x = numpy.mean(s)
y = numpy.median(s)
z = stats.mode(s)
print("The mean is ",x)
print("The mode is ",z)
print("The median is ",y)
