# question --> https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lkp = {}
        cur = 0
        sub = 0
        
        for ind, cha in enumerate(s):
            if cha not in lkp: 
                cur += 1
                lkp[cha] = ind
            else:
                sub = max(cur, sub)
                for k in lkp.copy(): 
                    if lkp[k] < lkp[cha]:
                        lkp.pop(k)
                lkp[cha] = ind
                cur = len(lkp)
                
        sub = max(cur, sub)
                
        return sub 
    
        # TC: O(|S|); SC: O(128 ~ 1)

# optimisation

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lkp = Counter()
        
        sub = 0
        l = 0
        
        for ind, ch in enumerate(s):
            lkp[ch] += 1
            while lkp[ch] > 1: 
                lkp[s[l]] -= 1
                l += 1
            sub = max(sub, ind - l + 1)
            
        return sub
                
        # TC: O(|S|); SC: O(128 ~ 1) 
        
