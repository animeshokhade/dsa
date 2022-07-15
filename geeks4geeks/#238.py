# question --> https://practice.geeksforgeeks.org/problems/uncommon-characters4932/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

class Solution:
    def UncommonChars(self, A, B):
        # code here
        lkpA = set(A)
        lkpB = set(B)

        ret = []

        for ch in A:
            if ch not in lkpB:
                ret.append(ch)

        for ch in B:
            if ch not in lkpA:
                ret.append(ch)

        ret = list(set(ret))
        ret.sort()

        return ''.join(ret) if ret else -1

        # TC: O((M + N)log(M + N)); SC: O(M + N)


# clean

class Solution:
    def UncommonChars(self, A, B):
        # code here
        a = set(A)
        b = set(B)
        return ''.join(sorted((a - b).union(b - a))) if a - b or b - a else -1

        # TC: O((M + N)log(M + N)); SC: O(M + N)