class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = []
        postfix = ''

        ind = 0
        n = len(A)

        priority = {
            '^': 1,
            '*': 2,
            '/': 2,
            '+': 3,
            '-': 3
        }

        for ind in range(n):
            if A[ind] == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()

            elif A[ind] in priority:
                while stack and stack[-1] != '(' and priority.get(A[ind]) >= priority.get(stack[-1]):
                    postfix += stack.pop()
                stack.append(A[ind])

            elif A[ind] == '(':
                stack.append(A[ind])

            else:
                postfix += A[ind]

        postfix += ''.join(stack)[::-1] if stack else ''

        return postfix

    # TC: O(N); SC: O(N)