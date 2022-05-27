# question --> https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def printTillN(self, N):
        # code here
        if N == 0: return 0
        self.printTillN(N - 1)
        print(N, end=' ')

    # TC: O(N); SC: O(N)
# end
