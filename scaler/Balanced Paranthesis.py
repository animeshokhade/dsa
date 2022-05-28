class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        self.stack = list()

    def solve(self, A):
        if len(A) != 0:
            for index, br in enumerate(A):
                if br == '{' or br == '(' or br == '[':
                    self.stack.append(br)
                else:
                    if len(self.stack) == 0:
                        return 0
                    elif (self.stack[-1] == '{' and br == '}') or (self.stack[-1] == '(' and br == ')') or (self.stack[-1] == '[' and br == ']'):
                        self.stack.pop()
                    else:
                        return 0
        if len(self.stack) != 0:
            return 0
        return 1

# alternative approach

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = []
        flag = True
        for c in A:
            if c == '(' or c == '{' or c == '[':
                s.append(c)
            else:
                if len(s) == 0:
                    return 0
                top = s[len(s)-1]
                s.pop()
                if not (c == ')' and top == '(' or c == '}' and top == '{' or c == ']' and top == '['):
                    flag = False
        if len(s) == 0 and flag:
            return 1
        else:
            return 0

