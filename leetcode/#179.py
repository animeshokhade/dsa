# question --> https://leetcode.com/problems/largest-number/

import functools
class Solution:
    def compare(self, string1: str, string2: str) -> int:
        if string1 + string2 >= string2 + string1:
            return -1
        else:
            return 1
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = functools.cmp_to_key(self.compare))

        return str(int(''.join(nums)))
        
        # TC: O(NlogN); SC: O(1)
        
# end 