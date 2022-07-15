# question --> https://practice.geeksforgeeks.org/problems/repeated-character2058/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

class Solution:
    def firstRep(self, s):
        # code here
        lkp = {}
        index = float('inf')

        for ind, char in enumerate(s):
            if char not in lkp:
                lkp[char] = ind
            else:
                index = min(index, lkp[char])

        return s[index] if index != float('inf') else -1

    # TC: O(|s|); SC: O(1)