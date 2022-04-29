# question --> https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        ans = False
        nums = set(nums)
        while not ans: 
            if i in nums:
                i += 1
                continue 
            ans = i 

        return ans 
        
        # TC: O(N); SC: O(N)
        
# Optimised Approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for index in range(len(A)):
            while ((A[index] >= 1) and (A[index] <= len(A)) and (A[index] != index + 1) and A[index] != A[A[index] - 1]):
                A[A[index] - 1], A[index] = A[index], A[A[index] - 1] 

        for index, num in enumerate(A):
            if (num != index + 1):
                return index + 1 
        
        return len(A) + 1
         
        # TC: O(N); SC: O(1)
        
# end 