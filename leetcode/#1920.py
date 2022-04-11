# question --> https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        iteration = len(nums)
        ans = list()
        for i in range(iteration):
            ans.append(nums[nums[i]])
        return ans
        

        