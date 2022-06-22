# question --> https://practice.geeksforgeeks.org/problems/common-elements1132/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        # your code here
        return sorted(list(set(A).intersection(set(B)).intersection(set(C))))

        # TC: O(NlogN); SC: O(A + B + C)

# optimised

class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        # your code here
        p1, p2, p3 = 0, 0, 0

        cmn = []
        while p1 < n1 and p2 < n2 and p3 < n3:
            if A[p1] == B[p2] == C[p3]:
                cmn.append(A[p1])
                while p1 < n1 - 1 and A[p1] == A[p1 + 1]:
                    p1 += 1
                while p2 < n2 - 1 and B[p2] == B[p2 + 1]:
                    p2 += 1
                while p3 < n3 - 1 and C[p3] == C[p3 + 1]:
                    p3 += 1
            cur_min = min(A[p1], B[p2], C[p3])
            if A[p1] == cur_min:
                p1 += 1
            if B[p2] == cur_min:
                p2 += 1
            if C[p3] == cur_min:
                p3 += 1
        return cmn

    # TC: O(A + B + C); SC: O(A + B + C)
