# for arrays ending at jth index
# forward iteration

import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        n = len(A)
        maxElement = max(A)
        iterations = int(math.log(maxElement, 2)) + 1

        for i in range(iterations):
            setBitTracker = 0
            for j in range(n):
                if (A[j] >> i) & 1:
                    setBitTracker = j + 1
                ans += (setBitTracker) * pow(2, i)

        return ans % (pow(10, 9) + 7)

