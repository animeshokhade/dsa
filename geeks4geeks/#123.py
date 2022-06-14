# question --> https://practice.geeksforgeeks.org/problems/automorphic-number4721/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def is_AutomorphicNumber(self, n):
        # Code here
        base = 0
        temp = n
        while temp:
            base += 1
            temp //= 10
        sqr = n * n
        if sqr % pow(10, base) == n: return 'Automorphic'
        return 'Not Automorphic'

    # TC: O(logN); SC: O(1)
