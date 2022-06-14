# question --> https://practice.geeksforgeeks.org/problems/number-of-diagonals1020/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def diagonals(self, n):
        # code here
        return (n * (n - 3)) // 2

    # TC: O(1); SC: O(1)