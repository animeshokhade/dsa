# question --> https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def reverse(self, A, D, N):
        l = D
        r = N
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1

    def rotateArr(self, A, D, N):
        # Your code here
        l, r = 0, N - 1
        D %= N

        self.reverse(A, 0, N - 1)
        self.reverse(A, 0, N - D - 1)
        self.reverse(A, N - D, N - 1)

        return A

        # TC: O(N); SC: O(1)