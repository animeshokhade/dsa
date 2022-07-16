class Solution:
    # @param A : list of integers
    # @return an integer
    def nsl(self, A):
        stack = []
        n = len(A)
        ret = [-1] * n

        for ind in range(n):
            while stack and A[ind] <= A[stack[-1]]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def nsr(self, A):
        stack = []
        n = len(A)
        ret = [n] * n

        for ind in range(n - 1, -1, -1):
            while stack and A[ind] <= A[stack[-1]]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def largestRectangleArea(self, A):
        l = self.nsl(A)
        r = self.nsr(A)
        rec = float('-inf')

        for ind, ele in enumerate(A):
            p1 = l[ind]
            p2 = r[ind]
            w = p2 - p1 - 1
            h = ele

            rec = max(rec, w * h)

        return rec

    # TC: O(N); SC: O(N)

# clean

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []

        n = len(A)
        rec = 0
        temp = 0
        area = 0

        ind = 0
        while ind < n:
            if not stack or A[stack[-1]] < A[ind]:
                stack.append(ind)
                ind += 1
            else:
                temp = stack.pop()
                area = A[temp] * (ind if not stack else ind - stack[-1] - 1)
                rec = max(rec, area)

        while stack:
            temp = stack.pop()
            area = A[temp] * (ind if not stack else ind - stack[-1] - 1)
            rec = max(area, rec)

        return rec

        # TC: O(N); SC: O(N)


'''
We make a stack to store NSL indices while the current index represents NSR. 

We traverse the histogram height array. For each height, we make a 
check whether that height could be a potential NSL or not. There are two 
conditions which help us do that -

1. Empty Stack 
    No NSL for current element, so current element can be a NSL for future elements. 

2. cur element >= stack top element 
    If the cur element was smaller then it becomes the NSR for the stack top element. 

If the above two conditions are not met, then we have found NSR. So we pop the stack top
and calculate area for that histogram. 

Case 1: Non Empty Stack 
    Stack top becomes NSL
    Cur element index becomes NSR 
    width = (NSR - 1) - (NSL + 1) + 1 = NSR - NSL - 1 

Case 2: Empty Stack 
    -1 becomes NSL 
    current index becomse NSR 
    width = (NSR - 1) - (-1 + 1) + 1 = NSR 

The stack top element which is popped provides the height for this area. 

Once the traversal is complete, we empty the stack considering every popped 
stack element with n as its NSR and stack top as its NSL. For the last stack element 
NSL -> 0 and NSR -> n. 

We maintain a max_area variable and return it. 
'''