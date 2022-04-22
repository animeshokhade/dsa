# question --> https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNaturalNumbers = (len(nums) * (len(nums) + 1)) // 2
        return sumNaturalNumbers - sum(nums) 
        
        # TC: O(N); SC: O(1)
        
# end 