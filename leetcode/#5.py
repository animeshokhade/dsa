# question --> https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pal = ''
        for i in range(n):
            # checking for odd length palindromes
            l, r = i - 1, i + 1
            while (l >= 0) and (r < n) and (s[l] == s[r]):
                l -= 1
                r += 1
            
            if r - l - 1 > len(pal):
                pal = s[l + 1:r]  
            elif r - l - 1 == len(pal):
                if s.index(pal[0]) > l: 
                    pal = s[l + 1:r]
                    
        for i in range(n):
            # checking for even length palindromes
            l, r = i - 1, i
            while (l >= 0) and (r < n) and (s[l] == s[r]):
                l -= 1
                r += 1
                
            if r - l - 1 > len(pal):
                pal = s[l + 1:r] 
            elif r - l - 1 == len(pal):
                if s.index(pal[0])> l: 
                    pal = s[l + 1:r]
                    
        return pal 
        
        # TC: O(N^2); SC: O(N)
        
# end 