# question --> https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def gcd(self, A, B):
        # code here
        if B == 0:
            return A
        return self.gcd(B, A % B)

    # TC: O(log(max(A, B))); SC: O(log(max(A, B)))

# non-recursive

class Solution:
    def gcd(self, A, B):
        # code here
        while B:
            x = B
            B = A % B
            A = x
        return A

    # TC: O(log(max(A, B))); SC: O(1)
