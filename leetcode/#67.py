# question --> https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        iterations = max(len(a), len(b))
        ans, carry = '', 0
        
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
            
        else:
            a = '0' * (len(b) - len(a)) + a 
            
        revA, revB = a[::-1], b[::-1]
        
        for i in range(iterations):
            tempSum = (int(revA[i]) + int(revB[i]) + carry) % 2
            carry = (int(revA[i]) + int(revB[i]) + carry) // 2
            ans += str(tempSum)
            
        if str(carry) == '1':
            ans += str(carry)
            
        return ans[::-1] 
        
        # TC: O(N); SC: O(S)
        
# end