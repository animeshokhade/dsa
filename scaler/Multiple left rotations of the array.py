class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        iterations = len(B)
        size = len(A)
        ans = []
        for iteration in range(iterations):
            B[iteration] %= size
            newArray = A[B[iteration]:] + A[:B[iteration]]
            ans.append(newArray)
        return ans


