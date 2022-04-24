# question --> https://leetcode.com/problems/add-digits/

class Solution:
    def summ(self, num: int) -> int:
        if num // 10 == 0: 
            return num % 10
        return self.summ(num // 10) + num % 10
    def addDigits(self, num: int) -> int:
        ans = self.summ(num)
        if ans > 9:
            return self.addDigits(ans)
        return ans
            
        # TC: O(logN - base10); SC: O(logN - base10)
        
# Optimised Approach

class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 != 0: 
            return num % 9
        elif num == 0: 
            return 0
        return 9
        
        # TC: O(1); SC: O(1)
        
# end 
        