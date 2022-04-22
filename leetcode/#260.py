# question --> https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lookup = set()

        for number in nums: 
            if number in lookup: 
                lookup.remove(number)
            elif number not in lookup: 
                lookup.add(number)

        return sorted(lookup) 
        
        # TC: O(N); SC: O(N)

# Optimised Approach - 01

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums: 
            xor ^= num
            
        firstSetBit = 0 
                
        for firstSetBit in range(32):
            if (1 << firstSetBit) & xor: 
                break
                
        num1 = 0
        for num in nums: 
            if (1 << firstSetBit) & num: 
                num1 ^= num
                
        return [min(num1, num1^xor), max(num1, num1^xor)]
        
        # TC: O(N); SC: O(1)
        
# Optimised Approach - 02

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums: 
            xor ^= num
            
        firstSetBit = (xor & (xor - 1)) ^ xor
                
        num1 = 0
        for num in nums: 
            if firstSetBit & num: 
                num1 ^= num
                
        return [min(num1, num1^xor), max(num1, num1^xor)]
        
        # TC: O(N); SC: O(1)
        
# end 
        
         

