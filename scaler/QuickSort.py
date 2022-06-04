class Solution:
    # @param A : list of integers
    # @return a list of integers
    def rearrange(self, A, start, end):
        left = start + 1
        right = end
        while left <= right:
            if A[left] < A[start]:
                left += 1
            elif A[right] > A[start]:
                right -= 1
            else:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        A[start], A[left - 1] = A[left - 1], A[start]
        return left - 1  # pivot

    def quicksort(self, A, start, end):
        if start >= end:
            return
        pos = self.rearrange(A, start, end)
        self.quicksort(A, start, pos - 1)
        self.quicksort(A, pos + 1, end)

    def solve(self, A):
        self.quicksort(A, 0, len(A) - 1)
        return A


'''
Average Case TC: O(NlogN)
Worst Case TC: O(N^2)
'''
