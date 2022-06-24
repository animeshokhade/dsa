# question --> https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bit = 0
        
        if n == 0:  
            return False 
        
        while n: 
            if n & 1: 
                bit += 1
                if bit > 1: 
                    return False
            n >>= 1
        return True 
    
        # TC: O(logN); SC: O(1)

# clean

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 0 else bin(n).count('1') == 1
        # TC: O(N); SC: O(1)