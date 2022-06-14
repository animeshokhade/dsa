# question --> https://practice.geeksforgeeks.org/problems/front-back-transformation1659/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:

    def convert(self, s):
        # code here
        s = list(s)
        n = len(s)
        for ind in range(n):
            if 'a' <= s[ind] <= 'z':
                s[ind] = chr(ord('a') + ord('z') - ord(s[ind]))
            else:
                s[ind] = chr(ord('A') + ord('Z') - ord(s[ind]))
        return ''.join(s)

        # TC: O(|s|); SC: O(1)
