# question --> https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        if n < numRows:
            return s

        pat = [''] * numRows
        rev = 1

        stepper = 0
        for ind, ele in enumerate(s):
            if stepper == 0 or stepper == numRows - 1:
                rev ^= 1

            pat[stepper] += ele

            if rev:
                stepper -= 1
            else:
                stepper += 1

        return ''.join(pat)

        # TC: O(|s|); SC: O(|s|)


# clean code

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pat = [''] * numRows
        rev = (numRows == 1) - 1
        stepper = 0

        for ind, ele in enumerate(s):
            pat[stepper] += ele
            if stepper == 0 or stepper == numRows - 1:
                rev *= -1
            stepper += rev

        return ''.join(pat)

        # TC: O(|s|); SC: O(|s|)
