# question --> https://practice.geeksforgeeks.org/problems/remove-common-characters-and-concatenate-1587115621/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

class Solution:

    # Function to remove common characters and concatenate two strings.
    def concatenatedString(self, s1, s2):
        # code here
        ret = ''
        lkp1 = set(s1)
        lkp2 = set(s2)

        for ch in s1:
            if ch not in lkp2:
                ret += ch

        for ch in s2:
            if ch not in lkp1:
                ret += ch

        return ret if ret else -1

        # TC: O(|s1| + |s2|); SC: O(|s1| + |s2|)