class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A.split('/')

        stack = []

        for ele in A:
            if ele == '.':
                continue
            elif stack and ele == '..':
                stack.pop()
            elif ele.isalpha():
                stack.append(ele)

        return '/' + '/'.join(stack)

    # TC: O(A); SC: O(Number of directories)