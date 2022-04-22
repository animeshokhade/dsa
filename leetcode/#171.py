# question --> https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        index = ['A',
                 'B',
                 'C',
                 'D',
                 'E',
                 'F',
                 'G',
                 'H',
                 'I',
                 'J',
                 'K',
                 'L',
                 'M',
                 'N',
                 'O',
                 'P',
                 'Q',
                 'R',
                 'S',
                 'T',
                 'U',
                 'V',
                 'W',
                 'X',
                 'Y',
                 'Z']

        summ, i = 0, 0
        for string in columnTitle:
            position = index.index(string) 
            weight = position + 1 
            summ += weight * (26 ** (len(columnTitle) - 1 - i))
            i += 1

        return summ

        # TC: O(N^2); SC: O(1)
        
# Optimised Approach

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        summ = 0
        for index, character in enumerate(columnTitle):
            weight = ord(character) - ord('A') + 1
            summ += weight * pow(26, (len(columnTitle) - 1 - index))
            
        return summ 
            
        # TC: O(N); SC: O(1)
        
# end 
