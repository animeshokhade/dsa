# question --> https://practice.geeksforgeeks.org/problems/binary-representation5003/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def getBinaryRep(self, n):
        # code here
        bin_rep = ''
        while n:
            bin_rep += str(n % 2)
            n //= 2
        bin_rep = bin_rep[::-1]
        return '0' * (30 - len(bin_rep)) + bin_rep

    # TC: O(logN); SC: O(1)