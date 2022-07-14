# question --> https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:

    def immediateSmaller(self, arr, n):
        # code here
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i] = arr[i + 1]
            else:
                arr[i] = -1

        arr[-1] = -1
        return arr

    # TC: O(N); SC: O(1)
