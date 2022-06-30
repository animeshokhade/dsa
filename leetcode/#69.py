# question --> https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        ret = 0

        while lo <= hi:
            mi = (lo + hi) // 2

            if mi * mi <= x:
                lo = mi + 1
                ret = mi

            else:
                hi = mi - 1

        return ret

        # TC: O(logN); SC: O(1)
