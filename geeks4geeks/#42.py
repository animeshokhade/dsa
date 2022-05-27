# question --> https://practice.geeksforgeeks.org/problems/series-ap5310/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def nthTermOfAP(self, A1, A2, N):
        # code here
        return A1 + (N - 1) * (A2 - A1)

    # TC: O(1); SC: O(1)
# end
