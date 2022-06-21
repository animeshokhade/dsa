# question --> https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    def remove_duplicate(self, A, N):
        # code here
        l = 0
        for r in range(1, N):
            if A[l] != A[r]:
                l += 1
                A[l] = A[r]
        return l + 1

    # TC: O(N); SC: O(1)
