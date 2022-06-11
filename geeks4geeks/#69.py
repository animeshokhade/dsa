# question --> https://practice.geeksforgeeks.org/problems/at-least-two-greater-elements4625/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def findElements(self, a, n):
        # Your code goes here
        a.sort()
        return a[:-2]

        # TC: O(NlogN); SC: O(N)
