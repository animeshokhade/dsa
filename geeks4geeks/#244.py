# question --> https://practice.geeksforgeeks.org/problems/find-the-odd-occurence4820/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here
        xor = 0
        for num in arr:
            xor ^= num

        return xor

    # TC: O(N); SC: O(1)