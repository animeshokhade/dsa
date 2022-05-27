# question --> https://practice.geeksforgeeks.org/problems/palindrome0746/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def is_palindrome(self, n):
        # Code here
        n = str(n)
        start, end = 0, len(n) - 1
        while start <= end:
            if n[start] != n[end]: return 'No'
            start += 1
            end -= 1
        return 'Yes'

# TC: O(N); SC: O(N)
# end
