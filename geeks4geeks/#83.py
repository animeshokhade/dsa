# question --> https://practice.geeksforgeeks.org/problems/split-strings5211/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def splitString(ob, S):
        # code here
        alpha = ''
        num = ''
        special = ''
        for char in S:
            if char.isalpha():
                alpha += char
            elif char.isdigit():
                num += char
            else:
                special += char
        return [alpha, num, special]

    # TC: O(|s|); O(1)