# question --> https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        setBit = 0
        while n: 
            if n & 1: 
                setBit += 1
            n >>= 1
        return setBit
                
        # TC: O(logN); SC: O(1) 