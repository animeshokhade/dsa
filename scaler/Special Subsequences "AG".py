class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        countG = 0
        ans = 0

        for g in range(len(A) - 1, -1, -1):
            if A[g] == 'G':
                countG += 1
            if A[g] == 'A':
                ans += countG

        return ans
