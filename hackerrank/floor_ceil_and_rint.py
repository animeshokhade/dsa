# question --> https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?h_r=profile
# default
import numpy
numpy.set_printoptions(legacy='1.13')

# my_code
a = list(map(float, input().split()))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

# end