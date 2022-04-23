# question --> https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = list()
        frequencyTracker = dict()
        n = len(nums)
        
        for num in nums:
            if num in frequencyTracker: 
                frequencyTracker[num] += 1
            else:
                frequencyTracker[num] = 1
                
        for element in frequencyTracker.keys():
            if frequencyTracker[element] > n // 3: 
                ans.append(element)
                
        return ans 
        
        # TC: O(N); SC: O(N)
        
# Optimised Approach --> Boyer Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        firstMajority, secondMajority = 0, 0
        firstCount, secondCount = 0, 0
        
        for num in nums: 
            if num == firstMajority: 
                firstCount += 1
            elif num == secondMajority: 
                secondCount += 1
            elif firstCount == 0: 
                firstMajority = num
                firstCount = 1
            elif secondCount == 0: 
                secondMajority = num
                secondCount = 1
            else:
                firstCount -= 1
                secondCount -= 1
                
        ans = list()
        test = len(nums) // 3
        
        tracker1, tracker2 = 0, 0
        
        for num in nums:
            if num == firstMajority:
                tracker1 += 1
            elif num == secondMajority:
                tracker2 += 1
        
        if tracker1 > test:
            ans.append(firstMajority)
        if tracker2 > test:
            ans.append(secondMajority)
        
        return ans
        
        # TC: O(N); SC: O(1)
        
# end 
