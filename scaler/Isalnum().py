class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for i in A:
            if not i.isalnum():
                return 0
        return 1


