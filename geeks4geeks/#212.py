# question --> https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1/?page=1&status[]=unsolved&category[]=Bit%20Magic&sortBy=submissions#

class Solution:

    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        # Your code here
        while k:
            n >>= 1
            k -= 1
        return n & 1

    # TC: O(logN); SC: O(1)