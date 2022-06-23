# question --> https://practice.geeksforgeeks.org/problems/prime-number2314/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:
    def isPrime (self, N):
        # code here
        if N == 1: return 0
        i = 2
        while i * i <= N: 
            if N % i == 0: 
                return 0
            i += 1
        return 1

    # TC: O(sqrt(N)); SC: O(1)