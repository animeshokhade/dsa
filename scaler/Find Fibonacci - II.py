class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A == 1: return 1
        if A == 0: return 0
        return self.findAthFibonacci(A - 1) + self.findAthFibonacci(A - 2)

# alternative approach

def Fibonacci(A):
    if A == 0:
        return 0
    elif A == 1:
        return 1
    else:
        return Fibonacci(A - 1) + Fibonacci(A - 2)

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        return Fibonacci(A)

# alternative approach

import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A == 1 or A == 2:
            return 1
        elif A == 0:
            return 0
        else:
            return self.findAthFibonacci(A - 1) + self.findAthFibonacci(A - 2)
