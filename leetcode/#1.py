# question --> https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum (self, nums: List[int], target: int) --> List[int]:
        # my code
        tracker = dict()

        # Making the element-index dictionary
        for index, num in enumerate(nums):
            if target - num in tracker:
                return [tracker[target - num], index]
            else:
                tracker[num] = index 
        
        return 

        # TC: O(N); SC: O(N)

# Editorial

class Solution:
    def twoSum (self, nums: List[int], target: int) --> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i] 
            if complement in hashmap:
                return [i, hashmap[complement]] 
            hashmap[nums[i]] = i 

        # TC: O(N); SC: O(N) 

# end