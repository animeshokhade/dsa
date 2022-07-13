class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        self.stack = []


    def solve(self, A):
        for br in A:
            if (
                br == '(' or \
                br == '{' or \
                br == '['
            ):
                self.stack.append(br)
            elif (
                self.stack and \
                ((br == ')' and self.stack[-1] == '(') or \
                 (br == '}' and self.stack[-1] == '{') or \
                 (br == ']' and self.stack[-1] == '['))
            ):
                self.stack.pop()
            else:
                return 0

        if self.stack:
            return 0

        return 1

# TC: O(N); SC: O(N)
