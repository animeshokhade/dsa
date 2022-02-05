# question --> https://leetcode.com/problems/plus-one/
# default

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # my_code
        for index in range(len(digits)):
            digits[index] = str(digits[index])
        digits = ''.join(digits)
        digits = int(digits)
        digits += 1
        digits = str(digits)
        new_digits = [string for string in digits]
        for index in range(len(new_digits)):
            new_digits[index] = int(new_digits[index])
        return new_digits

# end