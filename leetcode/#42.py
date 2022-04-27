# question --> https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        # leftMax
        leftMax = list()
        temp = float('-inf')
        for a in height: 
            if a > temp:
                temp = a
            leftMax.append(temp) 

        # rightMax 
        rightMax = list()
        temp = float('-inf')
        for a in range(len(height) - 1, -1, -1): 
            if height[a] > temp: 
                temp = height[a]  
            rightMax.append(temp)
        rightMax = rightMax[::-1]

        ans = 0 
        if height:
            for i in range(1, len(height) - 1):
                water = min(leftMax[i], rightMax[i]) - height[i]
                if water > 0:
                    ans += water 

        return ans 
        
        # TC: O(N); SC: O(N)
        
# Alternative Approach

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, len(height) - 1

        ans = 0

        maxLeft = float('-inf') 
        maxRight = float('-inf')

        while left <= right: 
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]

                else: 
                    ans += maxLeft - height[left]
                left += 1
            else: 
                if height[right] >= maxRight:
                    maxRight = height[right]
                else: 
                    ans += maxRight - height[right]
                right -= 1
        return ans 

        # TC: O(N); SC: O(N)
        
# end


        