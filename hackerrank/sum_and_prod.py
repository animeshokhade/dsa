# question --> https://www.hackerrank.com/challenges/np-sum-and-prod/problem?h_r=profile
# default
import numpy

# my_code
lst = list(map(int, input().split()))
array = list()
for n in range(lst[0]):
    row = list(map(int, input().split()))
    array.append(row)

temp = numpy.sum(array, axis = 0)
sol = numpy.product(temp)
print(sol)

# end