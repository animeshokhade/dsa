# question --> https://practice.geeksforgeeks.org/problems/got-tv-series3124/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def bitMultiply(self, N):
        # code here
        set_bits = 0
        temp = N
        while temp:
            if temp & 1:
                set_bits += 1
            temp >>= 1
        return set_bits * N

        # TC: O(logN); SC: O(1)
