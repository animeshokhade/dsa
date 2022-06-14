# question --> https://practice.geeksforgeeks.org/problems/sum-of-gp2120/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def sum_of_gp(self, n, a, r):
        # Code here
        if r == 1: return a * n
        return int((a * (1 - (r ** n))) / (1 - r))

    # TC: O(1); SC: O(1)
