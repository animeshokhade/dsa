# question --> https://practice.geeksforgeeks.org/problems/sum-of-odd-and-even-elements3033/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def find_sum(self, n):
        # Code here
        total = (n * (n + 1)) // 2

        if n & 1:
            n //= 2
            n += 1
            odd = n * n
            even = total - odd
        else:
            n //= 2
            even = n * (n + 1)
            odd = total - even

        return [odd, even]

    # TC: O(1); SC: O(1)