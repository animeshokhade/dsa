# question --> https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        
        l, r = 0, n - 1 
        while l < r: 
            if not ('a' <= s[l] <= 'z' or s[l].isdigit()):
                l += 1
            elif not ('a' <= s[r] <= 'z' or s[r].isdigit()):
                r -= 1
            else: 
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else: 
                    return False
                
        return True 
    
        # TC: O(N); SC: O(1) 