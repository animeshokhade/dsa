# question --> https://practice.geeksforgeeks.org/problems/swapping-triangles5209/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def swapTriangle(self, N, A):
        # code here
        for i in range(N):
            for j in range(len(A)):
                if i < j:
                    A[i][j], A[j][i] = A[j][i], A[i][j]
        return A

        # TC: O(N^2); SC: O(1)
