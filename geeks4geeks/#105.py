# question --> https://practice.geeksforgeeks.org/problems/npr4253/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def factorial(self, n, r):
        fact = 1
        fact1, fact2 = 1, 1
        for _ in range(1, n + 1):
            fact *= _
            if _ == n - r:
                fact1 = fact
        fact2 = fact
        return fact1, fact2

    def nPr(self, n, r):
        # code here
        f1, f2 = self.factorial(n, r)
        perm = int(f2 / f1)
        return perm

    # TC: O(N); SC: O(1)
