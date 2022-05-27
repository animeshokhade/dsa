# question --> https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    #Complete this function
    def printNos(self,N):
        #Your code here
        if N == 0:
            return
        self.printNos(N - 1)
        print(N, end = ' ')

        # TC: O(N); SC: O(N)
# end