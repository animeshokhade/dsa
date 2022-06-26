from collections import Counter
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        a = Counter(A)
        b = Counter()

        n = len(A)
        m = len(B)

        for i in range(n):
            b[B[i]] += 1

        win = m - n + 1
        per = 0

        for j in range(win):
            if a == b: 
                per += 1

            b[B[j]] -= 1
            if b[B[j]] == 0: 
                b.pop(B[j])

            if j + n < m: 
                b[B[j + n]] += 1
            
        return per 

        # TC: O(N); SC: O(26 ~ 1)