# question --> https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        bitMapCount = 1 << n
        
        ans = [[]]
        
        for bitRep in range(1, bitMapCount):
            subSet = []
            bitTracker = 0
            while bitRep: 
                if bitRep & 1: 
                    subSet.append(nums[bitTracker])
                bitRep >>= 1
                bitTracker += 1
            ans.append(sorted(subSet))
        
        return sorted(ans)
        
        # TC: O(logN(base2) * 2^N); SC: O(N)
        
# Cascading Approach

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        
        for num in nums: 
            ans += [x + [num] for x in ans]
            
        return sorted(ans)
        
        # TC: O(N * 2^N); SC: O(N * 2^N) 
        
# Recursion Approach

ans=[]
class Solution:
   
    def helper(self, nums, temp, index):
        
        if index == len(nums):
            ans.append(temp.copy())
            return
        self.helper(nums, temp, index + 1)
        temp.append(nums[index])
        self.helper(nums, temp, index + 1)
        temp.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        l = []
        ans.clear()
        nums.sort()
        self.helper(nums, l, 0)
        ans.sort()
        return ans
        
        # TC: O(N * 2^N); SC: O(N)
        
# end 


