class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_open, count_close = 0, 0
        for index, char in enumerate(A):
            if char == '(':
                count_open += 1
            elif char == ')':
                count_close += 1
            if count_close > count_open:
                return 0
        if count_open > count_close:
            return 0
        return 1

# alternative approach

class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        self.stack = list()

    def solve(self, A):
        if A[0] == ')':
            return 0
        if len(A) != 0:
            for index, char in enumerate(A):
                if char == '(':
                    self.stack.append(char)
                else:
                    if len(self.stack) != 0:
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
        count_open, count_close = 0, 0
        for index, char in enumerate(A):
            if char == '(':
                count_open += 1
            elif char == ')':
                count_close += 1
            if count_close > count_open:
                return 0
        if count_open - count_close > 0:
            return 0
        return 1