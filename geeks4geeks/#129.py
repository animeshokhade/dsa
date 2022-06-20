# question --> https://practice.geeksforgeeks.org/problems/compound-interest0235/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def getCompundInterest(self, P, T, N, R):
        # code here
        return int(P * pow((1 + R / (100 * N)), N * T))

    # TC: O(1); SC: O(1)
