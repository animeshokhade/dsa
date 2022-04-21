# question --> https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        q, r = n, 0
        binA = ''
        
        while q >= 1: 
            r = q % 2
            q //= 2
            binA += str(r)
            
        zeroes = 32 - len(binA)
        for _ in range(zeroes):
            binA += '0'
            
        i, j, ans = 31, 0, 0
        while j < 32: 
            if binA[j] == '1':
                ans += pow(2, i)
                
            i -= 1
            j += 1
            
        return ans
        
        # TC: O(logN); SC: O(logN)
        
# end 