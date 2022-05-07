# question --> https://leetcode.com/problems/total-hamming-distance/

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        i = 32
        ans = 0
        
        while i >= 0: 
            setBit = 0
            for num in nums:
                if num >> i & 1: 
                    setBit += 1
            ans += setBit * (len(nums) - setBit)
            i -= 1
            
        return ans 
        
        # TC: O(N); SC: O(1)

# end 