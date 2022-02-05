# question --> https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# default

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # my_code
        max_value = max(nums)
        count = 0
        if (len(nums) == 1):
            return 0
        for num in nums:
            if (num != max_value):
                if (max_value >= 2 * num):
                    count += 1
        if (count == len(nums) - 1):
            return nums.index(max_value)
        else:
            return -1

# end