class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = A.split()
        start, end = 0, len(ans) - 1
        while start <= end:
            ans[start], ans[end] = ans[end], ans[start]
            start += 1
            end -= 1

        return ' '.join(ans)

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A.strip()
        space = ' '
        sub_strings = []
        start, end = 0, 0

        for index in range(len(A)):
            if A[index] == space:
                if A[index - 1] != space:
                    end = index
                    sub_strings.append(A[start:end])
            else:
                if A[index - 1] == space:
                    start = index

        return ' '.join(sub_strings[::-1])

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.strip().split()

        return ' '.join(A[::-1])

# alternative approach

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.strip()
        ans, current = '', ''
        space = ' '
        n = len(A)
        start, end = n - 1, n - 1

        for i in range(n - 2, -1, -1):
            if A[i] == space:
                if A[i + 1] != space:
                    start = i + 1
                    current = A[start:end + 1]
                    if ans == '':
                        ans += current
                    else:
                        ans += space + current
            else:
                if A[i + 1] == space:
                    end = i

        return ans + space + A[:end + 1]