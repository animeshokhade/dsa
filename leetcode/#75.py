# question --> https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, mid = 0, 0
        end = len(nums) - 1
        
        while mid <= end: 
            if nums[mid] == 1: 
                mid += 1
            elif nums[mid] == 0: 
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 2: 
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
                
        return nums
        
        # TC: O(N); SC: O(1)
        
# end 