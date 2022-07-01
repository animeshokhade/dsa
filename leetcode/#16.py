# question --> https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = nums[0] + nums[1] + nums[2]
        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == target:
                    return cur_sum

                if abs(cur_sum - target) < abs(ret - target):
                    ret = cur_sum

                if cur_sum < target:
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                else:
                    while k < n and nums[k] == nums[k - 1]:
                        k -= 1

        return ret

        # TC: O(N^2); SC: O(1)