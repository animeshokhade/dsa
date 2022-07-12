# question --> https://practice.geeksforgeeks.org/problems/remove-all-characters-other-than-alphabets4923/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=latest#

class Solution:
    def removeSpecialCharacter(self, S):
        # code here
        ch = list(S)
        for i, c in enumerate(ch):
            if not c.isalpha():
                ch[i] = ''

        a = ''.join(ch)
        return a if a else -1

    # TC: O(|S|); SC: O(|S|)