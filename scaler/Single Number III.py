class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor = 0
        for index, number in enumerate(A):
            xor ^= number

        num1 = xor
        for index, number in enumerate(A):
            if ((xor & (xor - 1)) ^ xor) & number:
                num1 ^= number

        return sorted([num1, num1 ^ xor])

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        temp = 0
        B = sorted(A)
        for i in range(len(B) - 1):
            if (B[i] != B[i - 1]) and (B[i] != B[i + 1]):
                ans.append(B[i])

        if B[-1] != B[-2]:
            ans.append(B[-1])
        return ans

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        lookup = set()

        for number in A:
            if number in lookup:
                lookup.remove(number)
            elif number not in lookup:
                lookup.add(number)

        return sorted(lookup)

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor = 0
        for a in A:
            xor ^= a

        diff = 0
        for diff in range(32):
            if (1 << diff) & xor:
                break

        num1 = 0
        for num in A:
            if (1 << diff) & num:
                num1 ^= num

        return sorted([num1^xor, num1])