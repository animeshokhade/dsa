# question --> https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1/?page=1&status[]=unsolved&category[]=Bit%20Magic&sortBy=submissions#

class Solution:

    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        # Your code here
        if not n: return 0
        i = 1
        while n:
            if n & 1:
                return i
            n >>= 1
            i += 1

        # TC: O(logN); SC: O(1)