# question --> https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, max_ending_here = nums[0], nums[0]
        
        for index in range(1, len(nums)):
            temp = max_ending_here + nums[index]
            max_ending_here = max(temp, nums[index])
            max_so_far = max(max_so_far, max_ending_here)
            
        return max_so_far
        
        # TC: O(N); SC: O(1) 
        
# end