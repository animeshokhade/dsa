# question --> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        constDiff = arr[1] - arr[0]
        
        for index in range(1, n):
            if (arr[index] - arr[index - 1]) != constDiff: 
                return 0
            
        return 1
        
        # TC: O(NlogN); SC: O(1)
        
# end 
        