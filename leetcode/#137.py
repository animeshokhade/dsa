# question --> https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums: 
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        for ans in dictionary:
            if dictionary[ans] == 1:
                return ans 

        # TC: O(N); SC: O(N)

# Optimised Approach

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        commonMask = 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            commonMask = ~(ones & twos)
            ones &= commonMask
            twos &= commonMask
        return ones

        # TC: O(N); SC:O(1)

# end 