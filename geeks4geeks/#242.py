# question --> https://practice.geeksforgeeks.org/problems/check-for-subsequence4930/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

class Solution:
    def isSubSequence(self, A, B):
        # code here
        p1, p2 = 0, 0
        n, m = len(A), len(B)
        cnt = 0

        while p1 < n and p2 < m:
            if A[p1] == B[p2]:
                cnt += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        return cnt == n

        # TC: O(B); SC: O(1)