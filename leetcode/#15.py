# question --> https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []

        if set(nums) == {0}:
            return [[0, 0, 0]]

        a = 0
        nums.sort()
        zero = []

        while a < n - 2 and nums[a] <= 0:
            b = a + 1
            c = n - 1

            while b < c:
                cur_sum = nums[a] + nums[b] + nums[c]

                if cur_sum == 0:
                    zero.append([nums[a], nums[b], nums[c]])

                    b += 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1

                    c -= 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

                elif cur_sum < 0:
                    b += 1

                else:
                    c -= 1

            a += 1
            while a < n - 2 and nums[a] == nums[a - 1]:
                a += 1

        return zero

        # TC: O(N^2); SC: O(|zero|)

# clean

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        a = 0
        nums.sort()
        zero = []

        while a < n - 2 and nums[a] <= 0:
            while a > 0 and a < n - 2 and nums[a] == nums[a - 1]:
                a += 1
                continue

            b = a + 1
            c = n - 1

            while b < c:
                cur_sum = nums[a] + nums[b] + nums[c]

                if cur_sum == 0:
                    zero.append([nums[a], nums[b], nums[c]])

                    b += 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1

                    c -= 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

                elif cur_sum < 0:
                    b += 1

                else:
                    c -= 1

            a += 1

        return zero

        # TC: O(N^2); SC: O(|zero|)