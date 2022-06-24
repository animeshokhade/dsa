# question --> https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        tar = {}
        n = len(nums)
        
        for ind in range(n - 1):
            if nums[ind] == key: 
                if nums[ind + 1] in tar:
                    tar[nums[ind + 1]] += 1
                else: 
                    tar[nums[ind + 1]] = 1
        
        return max(tar.items(), key = lambda x: x[1])[0]
    
        # TC: O(N); SC: O(1)

# clean

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        tar = Counter()
        
        for a, b in zip(nums, nums[1:]):
            if a == key: 
                tar[b] += 1
            
        return max(tar, key = lambda x: tar[x])
        
        # TC: O(N); SC: O(1)