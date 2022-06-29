# question --> https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        n = len(nums)
        ret = 0

        for i in range(n):
            if i == 0 or nums[i] == nums[i - 1]:
                continue

            l, r = i - 1, i + 1
            while l >= 0 and nums[l] == nums[i]:
                l -= 1

            while r < n and nums[r] == nums[i]:
                r += 1

            if l >= 0 and r < n and nums[i] <= nums[l] and nums[i] <= nums[r]:
                ret += 1

            if l >= 0 and r < n and nums[i] >= nums[l] and nums[i] >= nums[r]:
                ret += 1

        return ret

    # TC: O(N); SC: O(1)

# clean

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ret = 0
        left = nums[0]
        n = len(nums)

        for i in range(1, n - 1):
            if left < nums[i] and nums[i] > nums[i + 1] \
                    or left > nums[i] and nums[i] < nums[i + 1]:
                ret += 1
                left = nums[i]

        return ret

        # TC: O(N); SC: O(1) 