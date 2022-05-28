class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        q, r = A, 0
        binA = ''
        while q >= 1:
            r = q % 2
            q //= 2
            binA += str(r)

        zeros = 32 - len(binA)
        for _ in range(zeros):
            binA += '0'

        i, j, ans = 31, 0, 0
        while j < 32:
            if binA[j] == '1':
                ans += 2 ** i
            i -= 1
            j += 1

        return ans



