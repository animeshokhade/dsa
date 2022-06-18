# question --> https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            base_n = self.myPow(x, -n)
            return 1 / base_n

        base_p = self.myPow(x, n // 2)

        if n & 1:
            return base_p * base_p * x

        return base_p * base_p

    # TC: O(logN); SC: O(logN)
