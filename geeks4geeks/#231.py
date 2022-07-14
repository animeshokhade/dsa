# question --> https://practice.geeksforgeeks.org/problems/merge-two-strings2736/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=latest#

class Solution:
    def merge(self, S1, S2):
        # code here
        ret = ''

        p1, p2 = 0, 0
        n, m = len(S1), len(S2)

        alt = True

        while p1 < n and p2 < m:
            if alt:
                ret += S1[p1]
                p1 += 1
                alt = False
            else:
                ret += S2[p2]
                p2 += 1
                alt = True

        while p1 < n:
            ret += S1[p1]
            p1 += 1

        while p2 < m:
            ret += S2[p2]
            p2 += 1

        return ret

        # TC: O(|S1| + |S2|); SC: O(|S1| + |S2|)