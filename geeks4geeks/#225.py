# question --> https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        # your code here
        x, y = 0, 1
        while n:
            x, y = y, x + y
            n -= 1
            print(x, end=' ')
        return ''

        # TC: O(N); SC: O(1)