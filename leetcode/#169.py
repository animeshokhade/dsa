# question --> https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for index in range(1, len(nums)):
            if majority == nums[index]:
                count += 1
            else: 
                count -= 1
                if count == 0: 
                    majority = nums[index]
                    count = 1
                    
        return majority 
        
        # TC: O(N); SC: O(1)
        
# end 
        