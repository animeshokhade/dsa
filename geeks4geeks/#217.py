# question --> https://practice.geeksforgeeks.org/problems/xor-of-all-elements0736/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def getXor(self, A, N):
        # code here
        ret = []
        xor = 0

        for a in A:
            xor ^= a

        for ind, ele in enumerate(A):
            xor ^= ele
            ret.append(xor)
            xor ^= ele

        return ret

    # TC: O(N); SC: O(1)