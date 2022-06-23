# question --> https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        ##Your code here
        if n == 0: return False
        set_bit = 0
        while n:
            if n & 1:
                set_bit += 1
                if set_bit > 1:
                    return False
            n >>= 1
        return True

    # TC: O(logN); SC: O(1)