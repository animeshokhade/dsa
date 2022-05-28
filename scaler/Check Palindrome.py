import sys
sys.setrecursionlimit(10**6)

def isPalindrome(A, start, end):
    if start >= end:
        return 1
    elif A[start] == A[end]:
        return isPalindrome(A, start + 1, end - 1)
    return 0

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        start, end = 0, len(A) - 1
        return isPalindrome(A, start, end)

# alternative approach

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        return Solution.isPalindrome(A, 0, len(A) - 1)

    def isPalindrome(A, start, end):
        if start >= end:
            return 1
        elif A[start] == A[end] and Solution.isPalindrome(A, start + 1, end - 1):
            return 1
        return 0

