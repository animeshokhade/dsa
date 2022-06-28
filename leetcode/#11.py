# question --> https://leetcode.com/problems/container-with-most-water/solution/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        water = 0

        while l < r:
            w = r - l
            h = min(height[r], height[l])
            water = max(water, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return water

        # TC: O(N); SC: O(1)