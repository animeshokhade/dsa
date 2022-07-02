# question --> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [0, 0]

        ret[0] = bisect_left(nums, target)
        if ret[0] == len(nums) or nums[ret[0]] != target:
            return [-1, -1]

        ret[1] = bisect_right(nums, target) - 1

        return ret

        # TC: O(logN); SC: O(1) 