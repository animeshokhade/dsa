# question --> https://www.hackerrank.com/challenges/np-min-and-max/problem?h_r=profile
# default
import numpy

# my_code
dimensions = list(map(int, input().split()))
array = list()
for dim in range(dimensions[0]):
    row = list(map(int, input().split()))
    array.append(row)

minimum = numpy.min(array, axis=1)
maximum = numpy.max(minimum)
print(maximum)

# end