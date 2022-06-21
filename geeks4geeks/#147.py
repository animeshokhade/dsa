# question --> https://practice.geeksforgeeks.org/problems/bubble-sort/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        # code here
        l = 0
        r = n - 1
        while l < r:
            while l < r:
                if arr[l] > arr[l + 1]:
                    arr[l], arr[l + 1] = arr[l + 1], arr[l]
                l += 1
            l = 0
            r -= 1

        return arr

        # TC: O(N^2); SC: O(1)
