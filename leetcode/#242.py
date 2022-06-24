# question --> https://leetcode.com/problems/valid-anagram/

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    # TC: O(|S| + |T|); SC: O(|S| + |T|)


# slightly optimised

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        freq = Counter(s)
        for ch in t: 
            if ch in freq: 
                freq[ch] -= 1
                if not freq[ch]:
                    del freq[ch]
        print(freq)
        if not freq: 
            return True 
        return False 
    
    # TC: O(|T|); SC: O(|S|)