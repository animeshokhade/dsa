# question --> https://practice.geeksforgeeks.org/problems/remove-character3815/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

class Solution:
    def removeChars(ob, string1, string2):
        # code here
        s = list(string1)
        lkp = set(string2)

        for ind, char in enumerate(s):
            if char in lkp:
                s[ind] = ''

        return ''.join(s)

        # TC: O(string1); SC: O(string2) 