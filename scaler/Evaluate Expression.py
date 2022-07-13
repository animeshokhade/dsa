class Solution:
    # @param A : list of strings
    # @return an integer
    def __init__(self):
        self.stack = ['#']


    def evaluate(self, num1, num2, opr):
        if opr == '+':
            return num2 + num1
        elif opr == '-':
            return num2 - num1
        elif opr == '*':
            return num2 * num1
        else:
            return num2 // num1


    def evalRPN(self, A):
        opr = {'+', '-', '/', '*'}

        for ind, ele in enumerate(A):
            if ele not in opr:
                self.stack.append(ele)

            elif self.stack[-1] != '#':
                num1 = int(self.stack.pop())
                num2 = int(self.stack.pop())
                res = self.evaluate(num1, num2, ele)
                self.stack.append(res)

        return self.stack[-1]

    # TC: O(N); SC: O(Operands)
    # N -> Array length