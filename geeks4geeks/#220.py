# question --> https://practice.geeksforgeeks.org/problems/strong-numbers4336/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def factorial(self, n):
        pro = 1
        while n:
            pro *= n
            n -= 1
        return pro

    def is_StrongNumber(self, n):
        # Code here
        fac = n
        fac_sum = 0
        while n:
            fac_sum += self.factorial(n % 10)
            n //= 10
        return int(fac == fac_sum)

    # TC: O(logN - base 10); SC: O(1)