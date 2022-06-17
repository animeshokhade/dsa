class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        ans = float('-inf')
        lookup = set(A)
        for ele in A:
            if ele - 1 not in lookup:  # start
                l = 0
                tmp = ele
                while tmp in lookup:
                    l += 1
                    tmp += 1
                ans = max(ans, l)
        return ans

    # TC: O(N); SC: O(N)
