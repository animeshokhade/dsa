# question --> https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def printFloydTriangle(self, N):
        #code here
        x = 1
        for n in range(1, N + 1):
            for m in range(n):
                print(x, end = ' ')
                x += 1
            print()

        return ''

    # TC: O(N); SC: O(1)