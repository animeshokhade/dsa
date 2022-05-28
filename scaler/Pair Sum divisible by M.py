class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = {}

        # modulo dictionary
        for a in A:
            if a % B in mod:
                mod[a % B] += 1
            else:
                mod[a % B] = 1

        # initialising answer for 0 modulo pair count
        if 0 in mod:
            ans = (mod[0]) * (mod[0] - 1) // 2
        else: ans = 0

        i, j = 1, B - 1
        while i < j:
            if i in mod and j in mod:
                ans += mod[i] * mod[j]
            i += 1
            j -= 1

        if not B & 1:
            if B >> 1 in mod:
                ans += (mod[B >> 1] * (mod[B >> 1] - 1)) // 2

        return ans % 1000000007

