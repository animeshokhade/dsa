# question --> https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_so_far = 0
        for index, ele in enumerate(nums):
            sum_so_far += ele
            nums[index] = sum_so_far
        return nums
    '''
    TC: O(N); SC: O(1)
    '''

    