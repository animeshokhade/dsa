# question --> https://practice.geeksforgeeks.org/problems/program-to-print-reciprocal-of-letters36233623/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def reciprocalString(self, S):
        # code here
        rec = ''
        for s in S:
            if s == ' ':
                rec += ' '
            else:
                if s.isupper():
                    rec += chr(ord('Z') - (ord(s) - ord('A')))
                else:
                    rec += chr(ord('z') - (ord(s) - ord('a')))

        return rec

    # TC: O(|S|); SC: O(|S|)