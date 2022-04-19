# question --> https://practice.geeksforgeeks.org/problems/palindrome-string0817/1/?page=1&difficulty[]=0&category[]=Strings&sortBy=submissions#

class Solution:
    def isPalindrome(self, S):
        # my code
        start, end = 0, len(S) - 1
        while start < end:
            if S[start] != S[end]:
                return 0
            start += 1
            end -= 1
        return 1
        
        # TC: O(S); SC: O(1)
        
# end
