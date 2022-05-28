class Solution:
    # @param A : long
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        ans = A
        for bitIndex in range(B):
            setBitCheck = 1 << bitIndex
            if A & setBitCheck:
                ans -= setBitCheck
        return ans

# alternative approach

class Solution:
    # @param A : long
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        q, r = A, 0
        binA = ''
        while q >= 1:
            r = q % 2
            binA += str(r)
            q //= 2

        binB = '0' * B + '1' * (len(binA) - B)
        ans = ''

        for i in range(len(binA)):
            ans += str(int(binA[i]) & int(binB[i]))

        ans = str(ans)

        final_ans, power = 0, 1
        for i in range(len(ans)):
            if ans[i] == '1':
                final_ans += power
            power *= 2

        return final_ans

# alternative approach

class Solution:
    # @param A : long
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        ans = A
        bitIndex = 0
        for _ in range(B):
            if A & 1:
                ans -= 1 << bitIndex
            bitIndex += 1
            A >>= 1
        return ans



