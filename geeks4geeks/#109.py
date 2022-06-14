# question --> https://practice.geeksforgeeks.org/problems/full-prime2659/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def isPrime(self, N):
        i = 2
        while i * i <= N:
            if N % i == 0:
                return 0
            i += 1
        return 1

    def fullPrime(self, N):
        # code here
        if self.isPrime(N):
            while N:
                digit = N % 10
                if digit == 0 or digit == 1 or not self.isPrime(digit):
                    return 0
                N //= 10
            return 1
        return 0

    # TC: O(sqrt(N)); SC: O(1)
