# question --> https://practice.geeksforgeeks.org/problems/sum-of-ap-series4512/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def sum_of_ap(self, n, a, d):
        # Code here
        return int(n * ((2 * a + (n - 1) * d) / 2))

    # TC: O(1); SC: O(1)
