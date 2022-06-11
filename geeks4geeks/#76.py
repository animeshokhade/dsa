# question --> https://practice.geeksforgeeks.org/problems/average4856/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def streamAvg(self, arr, n):
        # code here
        summ = 0
        for ind, ele in enumerate(arr):
            summ += ele
            arr[ind] = summ / (ind + 1)
        return arr

    # TC: O(N); SC: O(1)
