class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        ans = []
        for s in range(n):
            for e in range(s, n):
                subArray = A[s:e + 1]
                m = len(subArray)
                flag = True
                for num in subArray:
                    if num < 0:
                        flag = False
                if flag:
                    if m > len(ans):
                        ans = subArray
        return ans



