# question --> https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I': 1,
            'V': 5,
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        ans = 0
        n = len(s)
        for ind, cha in enumerate(s): 
            if cha != 'I' and cha != 'X' and cha != 'C':
                ans += rom[cha]
            elif cha == 'I':
                if ind < n - 1 and (s[ind + 1] == 'V' or s[ind + 1] == 'X'):
                    ans -= 1
                else:
                    ans += 1
            elif cha == 'X':
                if ind < n - 1 and (s[ind + 1] == 'L' or s[ind + 1] == 'C'):
                    ans -= 10
                else: 
                    ans += 10
            elif cha == 'C':
                if ind < n - 1 and (s[ind + 1] == 'D' or s[ind + 1] == 'M'):
                    ans -= 100
                else: 
                    ans += 100
                
        return ans 
                    
        # TC: O(|S|); SC: O(1)

# alternate approach -> clean

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I': 1,
            'V': 5,
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        ans = 0
        
        for a, b in zip(s, s[1:]):
            if rom[a] < rom[b]:
                ans -= rom[a]
            else:
                ans += rom[a]
                
        return ans + rom[s[-1]]
    
        # TC: O(|S|); SC: O(1)

