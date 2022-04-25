# question --> https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Base condition
        
        if n == 1: 
            return [0, 1] 
        
        # Recursive relation
        
        first_half = self.grayCode(n - 1)
        
        second_half = [(1 << (n - 1)) + num for num in reversed(first_half)]
        
        return first_half + second_half 
        
        # TC: O(2^N); SC: O(2^N)
        
# Alternative Approach

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = list()
        for code in range(1 << n):
            ans.append((code >> 1) ^ code)
        return ans 
        
        # TC: O(2^N); SC: O(2^N)
        
# end 

