# question --> https://practice.geeksforgeeks.org/problems/parallel-or-perpendicular4257/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def find(self, A, B):
        # Code here
        n = len(A)
        A_dot_B = 0

        for i in range(3):
            A_dot_B += A[i] * B[i]

        if A_dot_B == 0:
            return 2

        AxB = (A[1] * B[2] - A[2] * B[1]) ** 2 + (A[0] * B[2] - B[0] * A[2]) ** 2 + (A[0] * B[1] - A[1] * B[0]) ** 2

        if AxB == 0:
            return 1

        return 0

    # TC: O(1); SC: O(1)
