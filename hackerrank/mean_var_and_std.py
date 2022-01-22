# question --> https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?h_r=profile
# default
import numpy

# my_code
dimensions = list(map(int, input().split()))
array = list()
for dim in range(dimensions[0]):
    row = list(map(int, input().split()))
    array.append(row)

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
std = numpy.std(array)
std_limit = round(std, 11)

print(std_limit)

# end