import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return int(math.sqrt(A))

'''
Number of Perfect Squares under A = sqrt(A)
TC: O(logN)
Square Root is calculated using Binary Search 
'''

# alternate approach

import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return int(math.sqrt(A))

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        squares = 0
        i = 1
        while i * i <= A:
            squares += 1
            i += 1
        return squares
