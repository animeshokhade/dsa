# question --> https://practice.geeksforgeeks.org/problems/number-of-divisors1631/1/?page=3&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def count_divisors(self, N):
        # code here
        ans = 0
        i = 1
        while i * i <= N:
            if N % i == 0:
                if i % 3 == 0:
                    ans += 1
                if (N / i) % 3 == 0:
                    if i != N / i:
                        ans += 1
            i += 1
        return ans

    # TC: O(sqrt(N)); SC: O(1)
