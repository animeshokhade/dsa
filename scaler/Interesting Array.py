class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        count = 0
        for a in A:
            if a & 1:
                count += 1
        if count & 1:
            return 'No'
        return 'Yes'