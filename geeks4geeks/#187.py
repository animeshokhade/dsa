# question --> https://practice.geeksforgeeks.org/problems/bit-difference-1587115620/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        xor = a ^ b
        bit = 0
        while xor: 
            if xor & 1: 
                bit += 1
            xor >>= 1
        return bit 
        
        # TC: O(logN); SC: O(1)