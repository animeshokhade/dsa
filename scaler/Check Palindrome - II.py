class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        lst = list(str(A))
        test = dict()
        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        count = 0
        for key in test:
            if test[key] & 1 != 0:
                count += 1

        if count > 1:
            return 0
        return 1

# clean

import collections


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq = collections.Counter(A)  # hashing
        n = len(A)
        cnt = 0
        for char in freq:
            # even length arrays
            if n % 2 == 0 and freq[char] % 2 != 0:
                return 0

            # odd length arrays
            elif n % 2 == 1 and freq[char] % 2 == 1:
                cnt += 1
                if cnt > 1: return 0
        return 1

        # TC: O(N); SC: O(N)

