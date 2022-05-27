# question --> https://practice.geeksforgeeks.org/problems/sum-of-elements-in-a-matrix2000/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def sumOfMatrix(self, N, M, Grid):
        # code here
        Sum = 0
        for index in range(N):
            Sum += sum(Grid[index])
        return Sum

    # TC:O(N * M); SC: O(1)
# end
