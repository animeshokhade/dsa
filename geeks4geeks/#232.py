# question --> https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1/?page=1&status[]=unsolved&category[]=Hash&sortBy=submissions#

from collections import Counter


class Solution:

    # Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self, s):
        # code here
        freq = Counter(s)
        if len(freq) == len(s):
            return s[0]
        lkp = set([key for key in freq if freq.get(key) == 1])

        for ind, ele in enumerate(s):
            if ele in lkp:
                return ele

        return -1

        # TC: O(|s|); SC: O(distinct elements)