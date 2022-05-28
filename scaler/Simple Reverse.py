class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        i, j = 0, len(A) - 1
        ans = [i for i in A]

        while i < j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1

        return ''.join(ans)

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        return A[::-1]

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        i, j = 0, len(A) - 1
        ans = [i for i in A]

        while i < j:
            temp = ans[i]
            ans[i] = ans[j]
            ans[j] = temp
            i += 1
            j -= 1

        return ''.join(ans)


