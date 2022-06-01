# question --> https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        newString = ''
        for char in address:
            if char == '.':
                newString += '[' + char + ']'
            else:
                newString += char
        return newString

    '''
    TC: O(N)
    SC: O(N)
    '''
