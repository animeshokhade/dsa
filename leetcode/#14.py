# question --> https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        iterations = len(min(strs))
        ans = min(strs)
        
        if len(strs) == 1: 
            return strs[0]
        
        index = 0
        for index in range(iterations):
            temp = ans[index]
            for i in range(len(strs)):
                if strs[i][index] != temp: 
                    return ans[:index] 
        
        return ans[:index + 1]
        
        # TC: O(N^2); SC: O(N) 
        
# end 