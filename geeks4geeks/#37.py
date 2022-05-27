# question --> https://practice.geeksforgeeks.org/problems/swap-kth-elements5500/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:

    def swapKth(self, arr, n, k):
        # code here
        arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]

        return arr

    # TC: O(1); SC: O(1)
# end