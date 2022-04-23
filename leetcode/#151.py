# question --> https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        charArray = list(s.split())
        start, end = 0, len(charArray) - 1
        
        while start <= end: 
            charArray[start], charArray[end] = charArray[end], charArray[start] 
            start += 1
            end -= 1
            
        return ' '.join(charArray)
        
        # TC: O(N); SC: O(N)
        
# Alternative Approach

class Solution:
    def reverseWords(self, s: str) -> str:
        charArray = list(s.split())
        charArray = charArray[::-1]
        return ' '.join(charArray)
        
        # TC: O(N); SC: O(N)
        
# end 