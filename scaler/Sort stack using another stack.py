# insertion sort

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        stack = []

        while A:
            x = A.pop()

            while stack and stack[-1] > x:
                A.append(stack.pop())

            stack.append(x)

        return stack

        # TC: O(N^2); SC: O(N)

# merge sort

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def merge(self, stack1, stack2):
        ret = []

        while stack1 and stack2:
            if stack1[-1] > stack2[-1]:
                ret.append(stack1.pop())
            else:
                ret.append(stack2.pop())

        while stack1:
            ret.append(stack1.pop())

        while stack2:
            ret.append(stack2.pop())

        return ret[::-1]

    def mergesort(self, stack):
        n = len(stack)

        # base case
        if n <= 1:
            return stack

        temp = []

        for _ in range(n // 2):
            temp.append(stack.pop())

        stack = self.mergesort(stack)
        temp = self.mergesort(temp)

        return self.merge(stack, temp)

    def solve(self, A):
        return self.mergesort(A)

    # TC: O(NlogN); SC: O(N) 