class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        iterations = len(min(A))

    ans = min(A)
    if len(A) == 1:
        return A[0]
    for index in range(iterations):
        temp = ans[index]
        for i in range(len(A)):
            if A[i][index] != temp:
                return ans[:index]
    return ans[:index + 1]

