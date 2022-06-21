# question --> https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        # code here
        S = S.split('.')
        S = S[::-1]
        S = '.'.join(S)
        return S

        # TC: O(|S|); SC: O(|S|)