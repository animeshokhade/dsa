import functools
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def compare(self, string1: str, string2: str) -> int:
        if string1 + string2 >= string2 + string1:
            return -1
        else:
            return 1

    def largestNumber(self, A: list) -> str:
        A = [str(num) for num in A]
        A = sorted(A, key = functools.cmp_to_key(self.compare))

        return str(int(''.join(A)))

# alternative approach

import functools
class Solution:
    # @param A : tuple of integers
    # @return a strings

    def compare(self, a, b):
        if int(str(a)+str(b)) > int(str(b)+str(a)):
            return -1 # no need to swap
        elif int(str(a)+str(b)) < int(str(b)+str(a)):
            return 1 # Swap
        else:
            return 0 # do nothing

    def largestNumber(self, A):
        return str(int("".join([ str(i) for i in sorted(A, key=functools.cmp_to_key(self.compare))])))

# alternative approach

from fractions import Fraction


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, key=lambda n: Fraction(n, 10 ** len(str(n)) - 1), reverse=True)
        i = 0
        while i < len(A) - 1:
            if A[i] != 0:
                break
            else:
                i += 1

        ret = map(lambda x: str(x), A[i:])
        return ''.join(ret)
