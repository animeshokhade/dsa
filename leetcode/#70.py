# question --> https://leetcode.com/problems/climbing-stairs/

class Solution:
    def fibsum(self, n):
        a, b = 0, 1
        ret = 1
        while n: 
            a, b = b, a + b
            ret += a
            n -= 1
        return ret
    def climbStairs(self, n: int) -> int:
        return self.fibsum(n - 1)
    
    # TC: O(N); SC: O(N)