# question --> https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = 0, 0
        while S < len(s) and T < len(t):
            if s[S] == t[T]:
                S += 1
                T += 1
            else: 
                T += 1
        if S == len(s):
            return True
        return False 
        
        # TC: O(N); SC: O(1)
        
# end 