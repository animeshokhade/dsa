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
        
# cleaner BF

class Solution:
    def isPal(self, s: str, n: int, l: int, r: int) -> Tuple [int, int]:
        while l >= 0 and r < n: 
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
            
        return l + 1, r - 1
    
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ' '
        
        n = len(s)
        
        l, r = 0, 0
        pal = s[0]
        
        for i in range(n):
            l1, r1 = self.isPal(s, n, i, i)
            if r1 - l1 > r - l: 
                pal = s[l1:r1 + 1]
                l, r = l1, r1
            
            if i < n - 1 and s[i] == s[i + 1]:
                l1, r1 = self.isPal(s, n, i, i + 1)
                if r1 - l1 > r - l: 
                    pal = s[l1:r1 + 1]
                    l, r = l1, r1
                    
        return pal 
    
        # TC: O(|S|^2); SC: O(|S|)
                
        
# optimisation

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('@' + s + '$')
        n = len(t)
        
        pal_len = [0] * n
        centre = 0
        
        for i in range(1, n - 1):
            right_boundary = centre + pal_len[centre]
            d = i - centre
            mirror_index = centre - d
            
            pal_len[i] = right_boundary > i and \
                min(pal_len[mirror_index], right_boundary - i)
            
            # if pal_len[i] is updated with right_boundary - i
            # then there is a possibility of having a larger
            # palindrome size as the right boundary of the 
            # palidrome centred at centre overlaps with the 
            # right boundary of the sub-palindrome. 
            
            # expanding palindrome centred at i
            while t[i + pal_len[i] + 1] == t[i - pal_len[i] - 1]:
                pal_len[i] += 1
                
            # if palindrome centred at i expands past 
            # right_boundary, we update centre as the LPS
            # is now centred at i
            if pal_len[i] + i > right_boundary:
                centre = i 
                
        # LPS Centre and max_pal
        max_pal, lps_cen = max((pal, cen) \
                              for cen, pal in enumerate(pal_len))
        
        return s[(lps_cen - max_pal) // 2:(lps_cen + max_pal) // 2]
