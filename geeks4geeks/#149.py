# question --> https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    # Complete this function
    def power(self, N, R):
        # Your code here
        mod = 1000000007

        if R == 0:
            return 1

        base = self.power(N, R // 2)

        if R & 1:
            return (base * base * N) % mod
        return (base * base) % mod

        # TC: O(logN); SC: O(logN)
