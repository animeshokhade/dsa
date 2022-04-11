# question --> https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        iteration = len(str(x))
        
        for index in range(iteration):
            if string[index] != string[iteration - index - 1]:
                return False
        return True 
        
        # TC: O(N); SC: O(1)
        
# Editorial

class Solution:
    def isPalindrome(self, x: int) --> bool:
        # Special cases:
        # when x < 0, x is not a palindrome
        # Also, if the last digit of the number is 0,
        # in order to be a palindrome, 
        # the first digit of the number also needs to 
        # be 0
        # Only 0 satisfies this property
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False 
            
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
            
        # When the length is an odd number, we can get rid of the middle digit by revertedNumber // 10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123
        # since the middle digit doesn't matter in palindrome (it will always be equal to itself), we can simply get rid of it.
        
        return x == revertedNumber or x == revertedNumber // 10
        
        # TC: O(logN); SC: O(1)
        
        