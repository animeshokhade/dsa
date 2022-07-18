from collections import deque


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        a = deque(A)
        b = 0
        cyc = 0

        while a:
            if a[0] != B[b]:
                a.append(a.popleft())
            else:
                a.popleft()
                b += 1
            cyc += 1

        return cyc

        # TC: O(N^2); SC: O(N)


'''
Time Complexity Analysis: 

In the worst case, for every element, we traverse n - 1 elements to 
bring the last element at the 1st place. 

So, we pop after n - 1 traversals. That way, the total TC becomes the sum
of the following series - 

n - 1 + n - 2 + n - 3 ....
Therefore, n square. 
'''