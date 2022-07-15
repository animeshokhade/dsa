# question --> https://practice.geeksforgeeks.org/problems/find-first-repeated-character4108/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

class Solution:

    def firstRepChar(self, s):
        # code here
        lkp = set()

        for ch in s:
            if ch in lkp:
                return ch
            lkp.add(ch)

        return -1

        # TC: O(|s|); SC: O(|s|)