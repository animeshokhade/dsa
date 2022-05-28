class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):
        mapC = dict()
        ans = set()
        for h in C:
            if h in mapC:
                mapC[h] += 1
            else:
                mapC[h] = 1
        for k in mapC:
            if mapC[k] == B:
                ans.add(k)

        if len(ans) > 0:
            return sum(ans) % (10 ** 9 + 7)
        return -1
