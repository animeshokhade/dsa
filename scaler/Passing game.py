class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        stack = [B]
        for ele in C:
            if ele == 0:
                stack.pop()
            else:
                stack.append(ele)
        return stack[-1]

        # TC: O(C); SC: O(C) 