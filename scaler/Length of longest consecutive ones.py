class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        countOne = 0
        for i in range(len(A)):
            if A[i] == '1':
                countOne += 1

        count, maxCount = 0, 0
        for i in range(len(A)):
            l = i - 1
            r = i + 1
            L = R = 0
            while l >= 0:
                if A[l] == '1':
                    L += 1
                    l -= 1
                else: break

            while r < len(A):
                if A[r] == '1':
                    R += 1
                    r += 1
                else: break

            if A[i] == '1':
                maxCount = max(count, L + R + 1)
                count = maxCount

            else:
                if countOne > L + R:
                    maxCount = max(count, L + R + 1)
                    count = maxCount

                else:
                    maxCount = max(count, L + R)
                    count = maxCount

        return maxCount