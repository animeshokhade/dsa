# question --> https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1/?page=6&status[]=unsolved&sortBy=submissions#

class Solution:
    def nthFibonacci(self, n):
        # code here
        x, y = 0, 1
        mod = 1000000007
        while n:
            x, y = y, (x + y) % mod
            n -= 1
        return x % mod

        # TC: O(N); SC: O(N)