# question --> https://practice.geeksforgeeks.org/problems/extract-the-integers4428/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:

    def extractIntegerWords(self, s):
        # code here
        dig = []
        n = len(s)
        i = 0
        while i < n:
            tmp = ''
            while i < n and s[i].isdigit():
                tmp += s[i]
                i += 1
            if tmp:
                dig.append(tmp)
            i += 1
        return dig

        # TC: O(|S|); SC: O(|S|)
