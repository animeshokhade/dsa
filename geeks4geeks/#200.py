# question --> https://practice.geeksforgeeks.org/problems/product-of-maximum-in-first-array-and-minimum-in-second3943/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def find_multiplication (self, arr, brr, n, m) : 
        #Complete the function
        return max(arr) * min(brr)
        # TC: O(N + M); SC: O(1)