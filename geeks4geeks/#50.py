# question --> https://practice.geeksforgeeks.org/problems/reverse-digit0316/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def reverse_digit(self, n):
        # Code here
        size = len(str(n))
        power = pow(10, size - 1)
        ans = 0
        while n:
            ans += (n % 10) * power
            n //= 10
            power //= 10
        return ans

# TC: O(logN); SC: O(1)
# end
