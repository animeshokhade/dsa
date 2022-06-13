# question --> https://practice.geeksforgeeks.org/problems/small-factorial0854/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def find_fact(self, n):
        # Code here
        fact = 1
        for _ in range(n, 0, -1):
            fact *= _
        return fact

        # TC: O(N); SC: O(1)
