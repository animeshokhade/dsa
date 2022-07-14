# question --> https://practice.geeksforgeeks.org/problems/set-bits0143/1/?page=10&status[]=unsolved&sortBy=submissions#

class Solution:
    def setBits(self, N):
        # code here
        bit = 0
        while N:
            if N & 1:
                bit += 1
            N >>= 1

        return bit

        # TC: O(logN); SC: O(1)