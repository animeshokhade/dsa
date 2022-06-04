class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        L = float('inf')
        R = float('-inf')
        is_sorted = False
        for left in range(n):
            for right in range(left + 1, n):
                if A[left] > A[right]:
                    L = min(L, left)
                    R = max(R, right)
                    is_sorted = True

        if is_sorted:
            return [L, R]
        return [-1]


'''
TC: O(N^2)
SC: O(1)
'''

# optimised

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        is_sorted = True  # to check for -1 scenario

        # first unsorted index from the left
        for index in range(n - 1):
            if A[index + 1] < A[index]:
                i = index
                is_sorted = False
                break

        # first unsorted index from the right
        for index in range(n - 1, 0, -1):
            if A[index - 1] > A[index]:
                j = index
                is_sorted = False
                break

        if is_sorted: return [-1]

        # finding max and min for the isolated subarray to probe further
        Min = min(A[i:j + 1])
        Max = max(A[i:j + 1])

        # checking if all the elements left of the isolated subarray
        # are less than or equal to the Min
        left = 0
        while left <= i:
            if A[left] > Min:
                break
            left += 1

        # checking if all the elements right of the isolated subarray
        # are greater than or equal to the Max
        right = n - 1
        while right >= j:
            if A[right] < Max:
                break
            right -= 1

        return [left, right]


'''
TC: O(N)
SC: O(1)
'''

