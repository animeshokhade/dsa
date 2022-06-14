# question --> https://practice.geeksforgeeks.org/problems/perfect-number3759/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def factorial(self, N):
        fact = 1
        for _ in range(N, 0, -1):
            fact *= _
        return fact

    def isPerfect(self, N):
        # code here
        temp = N
        fact_sum = 0
        while temp:
            if temp % 10 != 0:
                fact_sum += self.factorial(temp % 10)
            temp //= 10
        return int(fact_sum == N)

        # Line 16: TC: O(1)
        # TC: O(logN) Base 10; SC: O(1)

