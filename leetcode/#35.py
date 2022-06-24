# question --> https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        floor = -1
        
        while lo <= hi: 
            mi = (lo + hi) // 2
            if nums[mi] == target: 
                return mi
            elif nums[mi] < target: 
                floor = mi
                lo = mi + 1
            else: 
                hi = mi - 1
                
        return floor + 1 
    
        # TC: O(logN); SC: O(1)

# alternate approach

from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
    
        # TC: O(logN); SC: O(1)