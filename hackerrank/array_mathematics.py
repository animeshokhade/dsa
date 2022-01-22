# question --> https://www.hackerrank.com/challenges/np-array-mathematics/problem?h_r=profile
# default
import numpy

# my_code
n, m = map(int, input().split())
lst0 = [n, m]
lst1 = list()
lst2 = list()
for x in range(lst0[0]):
    line1 = map(int, input().split())
    temp = line1
    lst1.append(list(temp))

a = list()
a = numpy.array(lst1)

for x in range(lst0[0]):
    line2 = map(int, input().split())
    temp = line2
    lst2.append(list(temp))

b = list()
b = numpy.array(lst2)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))

# end