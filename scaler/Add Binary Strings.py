class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        iterations = max(len(A), len(B))

        ans, carry = '', 0


        if len(A) > len(B):
            B = '0' * (len(A) - len(B)) + B

        else:
            A = '0' * (len(B) - len(A)) + A

        revA, revB = A[::-1], B[::-1]

        for i in range(iterations):
            tempSum = (int(revA[i]) + int(revB[i]) + carry) % 2
            carry = (int(revA[i]) + int(revB[i]) + carry) // 2
            ans += str(tempSum)

        if str(carry) == '1':
            ans += str(carry)

        return ans[::-1]

