# question --> https://www.hackerrank.com/challenges/np-eye-and-identity/problem?h_r=profile
# default
import numpy
numpy.set_printoptions(legacy='1.13')

# my_code
N, M = map(int, input().split())
print(numpy.eye(N, M))

# end