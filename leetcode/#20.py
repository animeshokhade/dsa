# question --> https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for br in s:
            if stk and br == ')' and stk[-1] == '(':
                stk.pop()
            elif stk and br == '}' and stk[-1] == '{':
                stk.pop()
            elif stk and br == ']' and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(br)

        if not stk:
            return 1
        return 0

        # TC: O(N); SC: O(N)

