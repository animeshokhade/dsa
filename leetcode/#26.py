# question --> https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = len(nums)
        index = 0
        while index != ans - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index + 1)
                ans -= 1
                continue
            index += 1
            
        return ans
        
        # TC: O(N); SC: O(1) 
        
# Editorial --> 2 Pointers approach 

# Since the array is already sorted, we keep two pointers: fast_runner and slow_runner. 

# As long as nums[slow_runner] == nums[fast_runner] we increment the fast_counter to skip the duplicates. 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        iteration = len(nums)
        
        for f in range(1, iteration):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]               
                fast += 1
            else: fast += 1
                
        return slow + 1
        
        # TC: O(N); SC: O(1)  