# question --> https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
    # TC: O(N); SC: O(N)