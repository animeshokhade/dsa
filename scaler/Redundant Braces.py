class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = ['#']
        for ind, ele in enumerate(A):
            if ele != ')':
                stack.append(ele)
            else:
                if stack[-1] == '(' and ele == ')':
                    return 1

                cnt = 0
                while stack[-1] != '(':
                    stack.pop()
                    cnt += 1

                if cnt == 1: return 1

                stack.pop()

        return 0

# clean and optimised 

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for ind, ele in enumerate(A):
            if ele != ')':
                stack.append(ele)
            else:
                cnt = 0
                while stack[-1] != '(':
                    stack.pop()
                    cnt += 1

                if cnt <= 1: return 1
                stack.pop()

        return 0

# alternative approach

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []

        for ind, ele in enumerate(A):
            opr = {'+', '-', '/', '*', '('}
            if ele.isalpha(): continue

            if ele != ')' and ele in opr:
                stack.append(ele)

            else:
                if stack[-1] == '(' and ele == ')':
                    return 1

                while stack[-1] != '(':
                    stack.pop()
                stack.pop()

        return 0

    # TC: O(N); SC: O(N)

