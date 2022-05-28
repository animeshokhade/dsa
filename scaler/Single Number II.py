import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        MSB = math.log(max(A), 2) + 1

        bit = 0
        ans = 0
        while bit <= MSB:
            count = 0
            for element in A:
                if element & (1 << bit):
                    count += 1
            if count % 3 != 0:
                ans += (1 << bit)
            bit += 1

        return ans

# alternate approach

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        dictionary = {}
        for a in A:
            if a in dictionary:
                dictionary[a] += 1
            else:
                dictionary[a] = 1
        for ans in dictionary:
            if dictionary[ans] == 1:
                return ans

