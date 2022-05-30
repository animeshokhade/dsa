class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if not A or B == 0: return 0
        A.sort()
        minDiff = float('inf')
        window = len(A) - B + 1
        for diff in range(window):
            minDiff = min(minDiff, A[diff + B - 1] - A[diff])
        return minDiff


'''
TC: O(N + NlogN) => O(NlogN)
SC: O(1)
'''
