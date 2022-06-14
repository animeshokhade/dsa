# question --> https://practice.geeksforgeeks.org/problems/pattern-printing1347/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def printPattern(self, N):
        #code here
        for _ in range(1, N + 1):
            print(_*'*', end = ' ')
        return ''

    # TC: O(N); SC: O(1)