# question --> https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x > 0 else -1
        x *= sign

        lo = -pow(2, 31)
        hi = -lo - 1

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        return 0 if rev < lo or rev > hi else rev * sign

        # TC: O(logx); SC: O(1)