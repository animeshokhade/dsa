class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxA = max(A)
        count = 0
        for integers in A:
            if integers != maxA:
                count += maxA - integers

        return count

    