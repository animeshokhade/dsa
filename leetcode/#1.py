# question --> https://leetcode.com/problems/two-sum/

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my code
        tracker = dict()
        ans = list()
        
        # Making the element-index dictionary
        for index, num in enumerate(nums):
            if target - num in tracker:
                ans.append(tracker[target - num])
                ans.append(index)
            else:
                tracker[num] = index 
                
        return ans 